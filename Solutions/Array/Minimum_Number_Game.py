class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        arr = nums[:]

        for i in range(0,len(nums),2):
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
        return arr