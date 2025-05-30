class Solution(object):
    # def binarySearch(self, nums, target):
    #     l, r = 0, len(nums) - 1

    #     while l <= r:
    #         mid = (l + r) // 2
    #         if nums[mid] == target:
    #             return True
    #         elif nums[mid] < target:
    #             l = mid + 1
    #         else:
    #             r = mid - 1
    #     return False

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsMap = set(nums)

        for num in range(0, len(nums)+1):
            if num not in numsMap:
                return num
