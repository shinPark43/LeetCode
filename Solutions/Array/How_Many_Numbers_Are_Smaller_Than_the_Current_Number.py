class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        hash_map = {}

        for i, v in enumerate(sorted_nums):
            if v not in hash_map:
                hash_map[v] = i

        return [hash_map[i] for i in nums]