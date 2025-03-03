class Solution(object):
    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = 0
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]

        for i in range(1, n):
            prefix_sum[i] = nums[i] + prefix_sum[i - 1] 

        for i in range(0, n):
            start = max(0, i - nums[i])
            if start:
                total += (prefix_sum[i] - prefix_sum[start - 1])
            else:
                total += prefix_sum[i]
        return total