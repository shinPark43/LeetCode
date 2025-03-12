class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # s.strip()
        words = s.split(" ")
        sorted_words = []
        for i in words:
            if i.isalpha():
                sorted_words.append(i)
        return ' '.join(sorted_words[0:k])