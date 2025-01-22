class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        other_then_val = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[other_then_val] = nums[i]
                other_then_val += 1
            
        return other_then_val