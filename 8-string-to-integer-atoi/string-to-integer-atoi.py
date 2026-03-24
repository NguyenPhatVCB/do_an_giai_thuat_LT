class Solution:
    def myAtoi(self, s):
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        i = 0
        n = len(s)

        # 1. bỏ khoảng trắng
        while i < n and s[i] == ' ':
            i += 1

        # nếu chuỗi rỗng
        if i == n:
            return 0

        # 2. xử lý dấu
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        # 3. đọc số
        num = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # 4. check overflow trước khi thêm
            if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num