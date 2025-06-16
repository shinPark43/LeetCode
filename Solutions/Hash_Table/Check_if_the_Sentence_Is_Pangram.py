class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        lower_case_letters = {}
        lower_case_count = 26

        for i in range(ord('a'), ord('z')+1):
            lower_case_letters[chr(i)] = 1
        
        for letter in sentence:
            if lower_case_letters[letter] == 1:
                lower_case_count -= 1
                lower_case_letters[letter] -= 1
        return lower_case_count == 0
