class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        answer = [0]*length
        prefix = 0
        suffix = sum(nums)
 
        for i in range(0, length):
            prefix += nums[i]
            answer[i] += abs(suffix - prefix)
            suffix -= nums[i]
            
        return answer 