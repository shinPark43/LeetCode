class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        hash_map = {}
        not_appear = []
        arr2_set = set(arr2)
        for element in arr1:
            if element not in arr2_set:
                not_appear.append(element)
            elif element not in hash_map:
                hash_map[element] = 1
            else:
                hash_map[element] += 1 
        not_appear.sort()
        result = []
        for element in arr2:
            for i in range(hash_map[element]):
                result.append(element)
        return result + not_appear
