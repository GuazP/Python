from time import time as tm
import numpy

def siev_np_guaz(n):
    def inkrementor():
        inkr = (4,2,4,2,4,6,2,6)
        while True:
            yield from inkr
    sieve = numpy.ones(n+1, dtype=numpy.bool)
    i = 7; j = 49; it = inkrementor()
    sieve[0:2] = 0; sieve[4::2] = 0; sieve[9::6] = 0; sieve[25::10] = 0;
    while j<n:
        if sieve[i]:
            i2 = i+i
            sieve[j::i2] = 0
        i += next(it); j = i*i;
    return numpy.nonzero(sieve)[0]


def siev_guaz(n):
    def inkrementor():
        inkr = (4,2,4,2,4,6,2,6)
        while True:
            yield from inkr
    if n < 100: return [i for i in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97) if i<n];
    res = [2, 3, 5]; s = bytearray([0]); i = 7; j = 49;
    s *= n
    s[9::6] = bytearray([1])*int((n-9)/6+1)
    s[25::10] = bytearray([1])*int((n-25)/10+1)
    it = inkrementor()
    def mo():
        s[j::i+i] = bytearray([1])*int((n-(j))/(i+i)+1)
        res.append(i)
    while j<n:
        mo() if not s[i] else None
        i += next(it); j = i*i
    return res + [g for g in range(i, n, 2) if not s[g]]

N = 10**8
tries = 1

time_start = tm()
for i in range(tries):
    test=siev_np_guaz(N)
    tim = round(tm()-time_start,5)
print ("Time to complete funkction guaz_numpy (in sec): ", tim, len(test))

time_start = tm()
for i in range(tries):
    test=siev_guaz(N)
    tim = round(tm()-time_start,5)
print ("Time to complete funkction guaz_numpy (in sec): ", tim, len(test))
