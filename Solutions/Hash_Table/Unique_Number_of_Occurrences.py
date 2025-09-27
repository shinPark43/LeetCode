class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hash_table = {}

        for num in arr:
            if num not in hash_table:
                hash_table[num] = 1
            else:
                hash_table[num] += 1
        
        result = set([])

        for num, val in hash_table.items():
            if val not in result:
                result.add(val)
            else:
                return False
        return True
