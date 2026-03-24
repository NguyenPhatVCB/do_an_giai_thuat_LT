class Solution:
    def generateParenthesis(self, n):
        result = []
        
        def backtrack(current, open_count, close_count):
            # nếu đủ độ dài
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # thêm "(" nếu còn quyền thêm
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            
            # thêm ")" nếu hợp lệ
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
        
        backtrack("", 0, 0)
        return result