class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start_idx = 0
        length = len(nums) - 1
        total = 0

        nums.sort()

        while start_idx < length:
            if (nums[start_idx] + nums[length]) < target:
                total += (length - start_idx)
                start_idx += 1
            else:
                length -= 1

        return total