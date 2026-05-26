class Solution:
    def restoreIpAddresses(self, s):

        res = []
        path = []

        def valid(part):
            return len(part) > 0 and int(part) <= 255 and (part == "0" or part[0] != "0")

        def backtrack(start, dots):

            if dots == 3:
                last = s[start:]
                if valid(last):
                    res.append(".".join(path + [last]))
                return

            for i in range(start, min(start + 3, len(s))):

                part = s[start:i + 1]

                if valid(part):
                    path.append(part)
                    backtrack(i + 1, dots + 1)
                    path.pop()

        backtrack(0, 0)
        return res