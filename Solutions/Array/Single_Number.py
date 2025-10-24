class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = 0
        for num in nums:
            unique = unique ^ num
        return unique
