class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_table = {}
        for num in nums:
            if num not in num_table:
                num_table[num] = 1
            else:
                num_table[num] += 1
        total = 0 
        for num, count in num_table.items():
            if count == 1:
                total += num
        return total
