class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowel = {'a', 'e', 'i', 'o', 'u'}
        hash_map = {}
        vowel_max = 0
        consonant_max = 0
        
        for i in range(ord('a'), ord('z')+1):
            hash_map[chr(i)] = 0

        for char in s:
            hash_map[char] += 1
            if char in vowel and hash_map[char] > vowel_max:
                vowel_max = hash_map[char]
            elif char not in vowel and hash_map[char] > consonant_max:
                consonant_max = hash_map[char]
        return vowel_max + consonant_max
