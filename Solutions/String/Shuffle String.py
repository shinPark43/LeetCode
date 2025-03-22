class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        word_list = ['']*len(s)

        for i in range(len(indices)):
            word_list[indices[i]] = s[i]

        return ''.join(word_list)
        
