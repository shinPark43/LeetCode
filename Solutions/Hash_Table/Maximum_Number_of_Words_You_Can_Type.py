class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        word_list = text.split(' ')

        total = 0

        for word in word_list:
            word_set = set(word)
            isBroken = True
            for letter in brokenLetters:
                if letter in word_set:
                    isBroken = False
                    break
            if isBroken:
                total += 1
        return total
