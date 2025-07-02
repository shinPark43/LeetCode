class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        frequency_dict = {}
        for num in nums:
            if num not in frequency_dict:
                frequency_dict[num] = 1
            else:
                frequency_dict[num] += 1
        result = []
        for i in range(1, len(nums)+1):
            temp = []
            for num in nums:
                if frequency_dict[num] == i:
                    temp.append(num)
            temp.sort(reverse=True)
            result += temp
        return result
