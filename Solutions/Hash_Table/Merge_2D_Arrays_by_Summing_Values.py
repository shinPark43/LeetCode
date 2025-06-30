class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        hash_map = {}
        for num in nums1:
            hash_map[num[0]] = num[1]
        
        for num in nums2:
            if num[0] not in hash_map:
                hash_map[num[0]] = num[1]
            else:
                hash_map[num[0]] += num[1]
        result = []
        for key, value in hash_map.items():
            result.append([key, value])
        result.sort()
        return result
