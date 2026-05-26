class Solution:
    def grayCode(self, n):

        res = [0]

        for i in range(n):
            add = 1 << i
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] + add)

        return res