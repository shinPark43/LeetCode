class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        nums_first_half = nums[:n]
        nums_second_half = nums[n:]
        insert_idx = 1
        for i in nums_second_half:
            nums_first_half.insert(insert_idx, i)
            insert_idx += 2
        return nums_first_half
