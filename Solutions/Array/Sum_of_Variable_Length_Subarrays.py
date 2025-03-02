class Solution(object):
    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = 0
        for i in range(0, n):
            start = max(0, i - nums[i])
            total += sum(nums[start:i+1])
        return total