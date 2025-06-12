class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        for x in range(len(nums)+1):
            smallest_index = -1
            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] >= x:
                    smallest_index = mid
                    high = mid - 1
                else:
                    low = mid + 1
            if len(nums) - smallest_index == x:
                return x
        return -1
