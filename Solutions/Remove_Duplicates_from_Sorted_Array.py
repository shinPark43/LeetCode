class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_index = 0

        for i in range(1, len(nums)):
            if (nums[unique_index] != nums[i]):
                unique_index += 1
                nums[unique_index] = nums[i]
        return unique_index + 1

        