class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 1000000007  # Modulo value
        odd = n // 2
        even = n - odd
        
        return (pow(4, odd, MOD) * pow(5, even, MOD)) % MOD
