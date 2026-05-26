class Solution:
    def partition(self, s):

        res = []
        path = []

        def is_pal(sub):
            return sub == sub[::-1]

        def backtrack(start):

            if start == len(s):
                res.append(path[:])
                return

            for i in range(start, len(s)):

                part = s[start:i + 1]

                if is_pal(part):
                    path.append(part)
                    backtrack(i + 1)
                    path.pop()

        backtrack(0)
        return res