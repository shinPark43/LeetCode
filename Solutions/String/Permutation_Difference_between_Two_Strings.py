class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        length = len(t)
        hash_map = {}
        total = 0
        for i in range(length):
            hash_map[t[i]] = i
        
        for i in range(length):
            total += abs(i - hash_map[s[i]])
        
        return total