class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        n = len(nums)

        for i in range(0, n):
            if bin(i).count('1') == k:
                total += nums[i]
        return total

