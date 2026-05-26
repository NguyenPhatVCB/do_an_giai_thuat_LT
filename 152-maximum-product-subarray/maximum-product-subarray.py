class Solution:
    def maxProduct(self, nums):
        maxP = nums[0]
        minP = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            cur = nums[i]

            temp_max = max(cur, maxP * cur, minP * cur)
            minP = min(cur, maxP * cur, minP * cur)

            maxP = temp_max

            res = max(res, maxP)

        return res