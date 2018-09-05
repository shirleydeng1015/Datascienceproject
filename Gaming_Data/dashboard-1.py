import sys
import csv
from decimal import Decimal
import datetime
import urllib.request
from urllib.request import Request, urlopen

#import urllib2.request
import re
import time
import html.parser
import json
import difflib


def main():
  steamcharts_site_list = [
    'https://steamcharts.com/top',
    'https://steamcharts.com/top/p.2',
    'https://steamcharts.com/top/p.3',
    'https://steamcharts.com/top/p.4'
  ]

  superdata_filename = 'Export-TitleLevel.csv'
  genre_filename = 'genres.csv'
  steamspy_api_call = 'http://steamspy.com/api.php?request=all'
  superdata_platforms = ['All Free-to-Play MMO Platforms','All Pay-to-Play MMO Platforms','All PC Platforms']
  
  now = datetime.datetime.now()

  ## Parse Superdata CSV file
  superdatadict = {}
  superdatadict = get_superdata(superdata_filename)
  
  ## Parse Genre CSV file
  genredict = {}
  genredict = get_genre_list(genre_filename)
  
  ## Get list of top games from Steamcharts
  ## Note: appid 480 is Valve test app
  appid_list = []
  appid_list = get_top_games(steamcharts_site_list)
  try:
    appid_list.remove('480')
  except ValueError:
    pass
  
  ## Get historical CCU data from Steamcharts
  steamchartsdict = {}
  for appid in appid_list:
    try:
      steamchartsdict[appid] = get_ccu_history(appid)
    except:
      err = sys.exc_info()[0]
      print("Downloading appid ", str(appid), " failed with error: ", err)
      raise err
  
  ## Get SteamSpy data
  steamspydict = {}
  steamspydict = get_steamspy(steamspy_api_call)
  
  ## Create CSV File
  print('Writing CSV file...')
  exportFilename = 'steamdashboard' + now.strftime('%Y-%m-%d-%H%M%S') + '.csv'
  exportFile = open(exportFilename,'w')
  wr = csv.writer(exportFile, quoting=csv.QUOTE_MINIMAL)
  
  month_list = get_month_list(now)
  
  ## CSV header row
  header_row = ['appid','Game','Genre','Developer'] + month_list + month_list + ['Players 2 Weeks','Players Forever']
  wr.writerow(header_row)
 
  # CSV data rows 
  for appid in appid_list:
    print('App ID:' + appid + '...',)
    if steamspydict.get(appid):
      name = steamspydict[appid].get('name').replace(u'\u2018',"'").replace(u'\u2019',"'")
      developer = steamspydict[appid].get('developer')
      players_2weeks = steamspydict[appid].get('players_2weeks')
      players_forever = steamspydict[appid].get('players_forever')
      superdata_name = None
    
      ## Fix weird naming issue in SteamSpy for H1Z1
      if appid == '295110':
        name = 'H1Z1: Just Survive'

      text = [appid, name, genredict.get(appid,'N/A'), developer]
      for month in month_list:
        text.append(steamchartsdict[appid].get(month, 0))
  
      if name not in superdatadict:
        for n in superdatadict.keys():
          seq = difflib.SequenceMatcher(None, name.lower(), n.lower(), False)
          ratio = seq.ratio() * 100
          if ratio > 97:
            print('found close Superdata match: ' + n + ' (match ratio: ' + str(ratio) + ')')
            superdata_name = n
            break
      else:
        print('found exact Superdata match')
        superdata_name = name
    
      if superdata_name == None:
        print('did not find SuperData match')

      for month in month_list:
        total = 0
      
        if superdata_name in superdatadict:  
          if month in superdatadict[superdata_name]:
            for platform in superdata_platforms:
              if platform in superdatadict[superdata_name][month].keys():
                total += superdatadict[superdata_name][month][platform]
        
        text.append('$' + str(total))
      
      text.extend([players_2weeks, players_forever])
      wr.writerow(text)
    
  print('Data exported to ' + exportFilename)
  exportFile.close()  
  sys.exit(0)

def send_request(site):
  headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
  }

  req = urllib.request.Request(site, data={}, headers=headers)
  ufile = urllib.request.urlopen(req)
  return ufile.read().decode("utf-8")

def get_top_games(site_list):
  appid_list = []
  for site in site_list:        
    print('Downloading: ' + site)

    text = send_request(site)
    appid_list.extend(re.findall(r'/app/(\d+)"', text))
    time.sleep(0.25)
  return appid_list
  
def get_ccu_history(appid):  
  site = 'https://steamcharts.com/app/' + str(appid)
  print('Downloading: ' + site)

  text = send_request(site)
  ccu_history = {}
  match = re.findall(r'"month-cell left">\s*(\w+\s\d+)\s*</td>\s*<td class="right num-f">(\d+.\d+)</td>', text)
  for data in match:
    month = data[0]
    ccu = data[1]
    if month not in ccu_history:
      ccu_history[month] = ccu
    else:
      print('Found duplicate Steamcharts data for appid: ', appid, month)
  time.sleep(0.25)
  return ccu_history

def get_genre_list(filename):
  print('Reading: ' + filename)
  genre_dict = {}
  csvfile = open(filename, 'r')
  reader = csv.reader(csvfile)
  for row in reader:
    genre_dict[row[0]] = row[2]
  return genre_dict

def get_superdata(filename):  
  print('Reading: ' + filename)
  datadict = {}
  csvfile = open(filename,'r')
  reader = csv.reader(csvfile)
  next(reader)
  for row in reader:
    try:
      if row[30]: 
        title = row[50]
        year = int(row[51])
        month = int(row[36])
        platform = row[37]
        revenue = Decimal(row[30][1:].replace(',',''))
        month_year = get_month_year(month, year)
        datadict[title]= datadict.get(title,{})
        datadict[title][month_year] = datadict[title].get(month_year,{})
        datadict[title][month_year][platform] = revenue
    except ValueError:
      pass
  csvfile.close()
  return datadict

def get_month_year(month, year):
  months = ['January','February','March','April','May','June','July','August','September','October','November','December']
  return months[month - 1] + ' ' + str(year)

def get_steamspy(api_call):
  print('Downloading: ' + api_call)
  text = send_request(api_call)
  return json.loads(text)

def get_month_list(now):
  month_list = []
  if now.month - 1 == 0:
    month = 12
    year = now.year - 2
  else:
    month = now.month - 1
    year = now.year - 1
  while month != now.month or year != now.year:
    month_list.append(get_month_year(month, year))
    month += 1
    if month > 12:
      month = 1
      year += 1
  return month_list

  


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
response = opener.open('http://httpbin.org/user-agent')

if __name__ == '__main__':
  main()
