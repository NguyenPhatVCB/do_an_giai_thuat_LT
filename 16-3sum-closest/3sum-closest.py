class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        
        closest = nums[0] + nums[1] + nums[2]  # giá trị ban đầu
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # cập nhật nếu gần target hơn
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  # chính xác bằng target
        
        return closest