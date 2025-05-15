class Solution(object):
    def lowerBound(self, nums):
        l, h = 0, len(nums) - 1
        index = h + 1

        while l <= h:
            mid = (l + h) // 2

            if nums[mid] < 0:
                l = mid + 1
            else:
                h = mid - 1
                index = mid
        
        return index


    def upperBound(self, nums):
        l, h = 0, len(nums) - 1
        index = h + 1

        while l <= h:
            mid = (l + h) // 2

            if nums[mid] <= 0:
                l = mid + 1
            else:
                h = mid - 1
                index = mid
        
        return index


    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return max(self.lowerBound(nums), n - self.upperBound(nums))
