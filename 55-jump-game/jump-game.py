class Solution:
    def canJump(self, nums):

        max_reach = 0

        for i in range(len(nums)):

            # Không thể tới vị trí hiện tại
            if i > max_reach:
                return False

            # Cập nhật vị trí xa nhất
            max_reach = max(max_reach, i + nums[i])

        return True