class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 0
        runningSum = []
        for i in nums:
            total += i
            runningSum.append(total)
        return runningSum