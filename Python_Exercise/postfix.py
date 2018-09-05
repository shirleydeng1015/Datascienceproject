import operator
file = open("input.txt","r")
#list the txt file
newlist = list(file.readlines(0))
#undersatnd how it is structured
# print(newlist)

#print out each list
for i in range(0, len(newlist)):
	print(newlist[i])
	i += 1


class Operations(object):
	'''Class the operations'''
	def __init__(self, line, items):
		self.name = name
		self.line = line
		self.items = items

