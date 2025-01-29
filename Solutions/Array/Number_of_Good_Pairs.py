class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        total = 0
        for i in range(0, length):
            for j in range(i + 1 , length):
                if nums[i] == nums[j]:
                    total += 1
        return total