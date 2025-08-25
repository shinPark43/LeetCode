class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map = {}
        for char in s:
            if char not in hash_map:
                hash_map[char] = 1
            else:
                hash_map[char] += 1
        result = 0
        for count in hash_map.values():
            if count > 2:
                if count % 2 == 0:
                    result += 2
                else:
                    result += 1
            else:
                result += count
        return result
