class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        total = 0

        nums.sort()

        while left < right:
            if (nums[left] + nums[right]) < target:
                total += (right - left)
                left += 1
            else:
                right -= 1
        return total