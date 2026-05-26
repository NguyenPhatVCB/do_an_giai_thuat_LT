class Solution:
    def myPow(self, x, n):

        # Nếu số mũ âm
        if n < 0:
            x = 1 / x
            n = -n

        result = 1

        while n > 0:

            # Nếu n lẻ
            if n % 2 == 1:
                result *= x

            x *= x
            n //= 2

        return result