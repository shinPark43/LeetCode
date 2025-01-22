class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        curr = 0
        for i in range(len(nums)):
            if curr == 0:
                stack.append(nums[curr])
                isFirst = False
                curr += 1
            elif nums[curr] != stack[-1]:
                stack.append(nums[curr])
                curr += 1
            elif nums[curr] == stack[-1]:
                nums.pop(curr)
                nums.append('_')
        return curr

        