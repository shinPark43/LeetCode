class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        nums.sort()
        min_avg = 51
        for i in range(len(nums)//2):
            result = (nums[i] + nums[len(nums) - 1 - i]) / 2
            if result < min_avg:
                min_avg = result
        return min_avg
