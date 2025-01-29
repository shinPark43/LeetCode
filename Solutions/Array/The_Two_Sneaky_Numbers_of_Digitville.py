class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sneaky = []
        for i in nums:
            if len(sneaky) == 2:
                break
            if nums.count(i) > 1 and sneaky.count(i) == 0:
                sneaky.append(i)
        return sneaky