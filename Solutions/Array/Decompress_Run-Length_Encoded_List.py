class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) / 2
        result = []
        for i in range(0, n):
            result.extend([nums[2*i+1]]*nums[2*i])
        return result