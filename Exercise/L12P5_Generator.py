#Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

#Sieve of Eratosthenes algorithm

def genPrimes():
    primeNumbers = range (2,2000)
    p=2
    yieldValue = 0
    while p in primeNumbers:
        for i in range(1, 2000/p):
            if i*p != p and i*p in primeNumbers:
                primeNumbers.remove(i*p)
        for i in primeNumbers:
            if i > p:
                p = i
                break
        yield primeNumbers[yieldValue]
        yieldValue += 1

#put the following in python shell:
foo=genPrimes()
foo.next()
foo.next()
foo.next()
