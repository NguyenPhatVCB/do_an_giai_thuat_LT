class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        
        # BƯỚC 1: tìm i
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Nếu tìm được i
        if i >= 0:
            # BƯỚC 2: tìm j
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            nums[i], nums[j] = nums[j], nums[i]
        
        # BƯỚC 3: đảo ngược phần sau i
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1