class Solution:
    def countAndSay(self, n):
        result = "1"
        
        for _ in range(1, n):
            new_str = ""
            count = 1
            
            for i in range(1, len(result)):
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    new_str += str(count) + result[i - 1]
                    count = 1
            
            # thêm nhóm cuối cùng
            new_str += str(count) + result[-1]
            
            result = new_str
        
        return result