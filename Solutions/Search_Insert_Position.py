class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except:
            if nums[0] > target:
                return 0
            for i in range(1, len(nums)):
                if nums[i-1] <= target and target < nums[i]:
                    return i
            return len(nums) 
