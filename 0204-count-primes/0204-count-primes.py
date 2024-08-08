class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        
        primes = [True] * n
        
        primes[0] = False
        primes[1] = False
        
        count = 0
        for i in range(2, n):
            if primes[i]:
                count += 1
                for i2 in range(i + i, n, i):
                    primes[i2] = False
                    
        return count
                    
                    