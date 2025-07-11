class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        num_table = {}
        for num in set(nums1):
            if num not in num_table:
                num_table[num] = 1
            else:
                num_table[num] += 1
        for num in set(nums2):
            if num not in num_table:
                num_table[num] = 1
            else:
                num_table[num] += 1
        for num in set(nums3):
            if num not in num_table:
                num_table[num] = 1
            else:
                num_table[num] += 1
        result = []
        for key, count in num_table.items():
            if count > 1:
                result.append(key)
        return result
