class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n

        # x^8 = x^4 * x^4
        # we can reuse computation
        res = 1

        while n >0:
            if n % 2 == 1:
                res *= x
            
            x *= x 
            n //= 2

        return res