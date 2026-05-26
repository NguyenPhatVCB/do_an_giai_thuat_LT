class Solution:
    def maxSubArray(self, nums):

        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):

            # Chọn bắt đầu mới hoặc cộng tiếp
            current_sum = max(nums[i], current_sum + nums[i])

            # Cập nhật kết quả lớn nhất
            max_sum = max(max_sum, current_sum)

        return max_sum