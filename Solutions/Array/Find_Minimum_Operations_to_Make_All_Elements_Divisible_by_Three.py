class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in nums:
            if i % 3 == 1:
                i -= 1
                count += 1
            elif i % 3 == 2:
                i += 1
                count += 1
        return count