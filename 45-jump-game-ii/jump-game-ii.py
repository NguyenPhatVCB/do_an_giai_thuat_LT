class Solution:
    def jump(self, nums):
        n = len(nums)
        jumps = 0
        end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            # khi tới giới hạn hiện tại → phải nhảy
            if i == end:
                jumps += 1
                end = farthest

        return jumps