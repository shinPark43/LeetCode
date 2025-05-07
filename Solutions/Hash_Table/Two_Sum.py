class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        n = len(nums)
        for i in range(n):
            hash_table[nums[i]] = i

        for i in range(n):
            num = target - nums[i]
            if num in hash_table and i != hash_table[num]:
                return [i, hash_table[num]]
