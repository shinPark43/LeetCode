class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        first_word_list = [word[0] for word in words]
        return "".join(first_word_list) == s
