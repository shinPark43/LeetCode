class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        total = 0
        for word in words:
            if word.find(pref) == 0:
                total += 1
        return total