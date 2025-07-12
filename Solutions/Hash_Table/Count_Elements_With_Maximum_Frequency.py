class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_table = {}
        max_frequency = 0
        for num in nums:
            if num not in count_table:
                count_table[num] = 1
            else:
                count_table[num] += 1
            if count_table[num] > max_frequency:
                max_frequency = count_table[num]
        total = 0
        for count in count_table.values():
            if count == max_frequency:
                total += count
        return total
