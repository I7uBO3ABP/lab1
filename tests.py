from bruteforce import bruteforceSearch
from BoyerMoore import BoyerMooreSearch
from KnuthMorrisPratt import KnuthMorrisPrattSearch
from RabinKarp import RabinKarpSearch
import timeit

#testfile = open('test.txt').readline()
#tests = [
   # [testfile, 'ab']
    # ['ЭТОИЭТОТ', 'ТОТ'],
    # ['aaabab', 'b'],
    # ['aefdgaabadfgagdgdab', 'ab'],
    # ['asfgdshgrtsfdgfasshtdsasf', 'as'],
    # ['fdsgsndhtryegfd', 'dsf'],
    # ['sdfghjhkfuyjthdgfgnmhfkyturytesfdgfbgshrg','y']
]

#for i in tests:
    #n = 100
    #print('Average time for 100 iterations')
    #print('String length - ', len(testfile), 'symbols')
    #print('bruteforce: ', timeit.timeit("bruteforceSearch(i[0], i[1])", globals=globals(), number=n)/n)
    #print('Boyer-Moore: ', timeit.timeit("BoyerMooreSearch(i[0], i[1])", globals=globals(), number=n)/n)
    #print('Rabin-Karp: ', timeit.timeit("RabinKarpSearch(i[0], i[1])", globals=globals(), number=n)/n)
    #print('Knuth-Morris-Pratt: ', timeit.timeit("KnuthMorrisPrattSearch(i[0], i[1])", globals=globals(), number=n)/n)
    

from KnuthMorrisPratt import KnuthMorrisPrattSearch
import timeit
def is_prime(n):
    """
    Функция, которая определяет, является ли число n простым.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


primes = []
num = 2

while len(primes) < 500:
    if is_prime(num):
        primes.append(str(num))
    num += 1

result = ''.join(primes)
orb1 = {}
orb = 0
for i in range(90):
    orb1[i] = len(KnuthMorrisPrattSearch(result,str(i + 10)))
    print(i + 10, len(KnuthMorrisPrattSearch(result,str(i + 10))))
    if orb1[i] > orb:
        orb = orb1[i]
        smth = i + 10
print(orb, smth)
