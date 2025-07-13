class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count_table = {}
        for num in nums:
            if num not in count_table:
                count_table[num] = 1
            else:
                count_table[num] += 1
        pair_count = 0
        remain = 0
        for key, val in count_table.items():
            if val > 1:
                pair_count += val // 2
                if val % 2 != 0:
                    remain += 1
            else:
                remain += 1
        return [pair_count, remain]
