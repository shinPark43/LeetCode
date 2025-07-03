class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count_table = {}
        for num in nums:
            if num not in count_table:
                count_table[num] = 1
            else:
                count_table[num] += 1
        for count in count_table.values():
            if count % 2 != 0:
                return False
        return True
