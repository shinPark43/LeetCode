class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        index = []
        vowels_in_s = []

        for i in range(len(s)):
            if s[i] in vowels:
                index.append(i)
                vowels_in_s.append(s[i])
        
        vowels_in_s.sort()
        s_to_list = list(s)
        for i in range(len(index)):
            s_to_list[index[i]] = vowels_in_s[i]
        return "".join(s_to_list)
