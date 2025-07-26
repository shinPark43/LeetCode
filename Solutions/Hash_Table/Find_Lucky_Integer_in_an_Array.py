class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        hash_map = {}
        for num in arr:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        max_lucky = -1
        for key, val in hash_map.items():
            if key == val and val > max_lucky:
                max_lucky = val
        return max_lucky
