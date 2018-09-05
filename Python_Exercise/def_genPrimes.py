def genPrimes():
    primes = [2]
    yield primes[0]
    newprime = 3
    while True:
        if all(newprime % x != 0 for x in primes):
            primes.append(newprime)
        if newprime == primes[-1]:
            yield primes[-1]
        newprime += 1

def genPrimes_Method():
    primes = []
    lastprime = 1
    while True:
        lastprime += 1
        for i in primes:
            if lastprime % i == 0:
                break
        else:
            primes.append(lastprime)
            yield lastprime