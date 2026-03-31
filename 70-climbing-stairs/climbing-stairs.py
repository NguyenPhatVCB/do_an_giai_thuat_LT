class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Trường hợp cơ bản
        if n <= 2:
            return n
        
        # f(n) = f(n-1) + f(n-2)
        # Ta chỉ cần lưu 2 giá trị gần nhất để tiết kiệm bộ nhớ
        first = 1  # tương ứng bậc 1
        second = 2 # tương ứng bậc 2
        
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
            
        return second