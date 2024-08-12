class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        primes = [True] * n
        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False
        
        return sum(primes)-2
