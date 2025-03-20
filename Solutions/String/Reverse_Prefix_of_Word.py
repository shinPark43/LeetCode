class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        ch_idx = word.find(ch)
        if ch_idx:
            return word[:ch_idx+1][::-1] + word[ch_idx+1:]
        return word