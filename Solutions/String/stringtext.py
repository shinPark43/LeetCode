class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = s.split()
        result = [""]*len(word_list)
        for word in word_list:
            idx = int(word[-1])
            result[idx - 1] = word[:-1]
        return " ".join(result)
