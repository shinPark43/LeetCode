class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphabet_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        code_list = []

        for word in words:
            encoded = ""
            for char in word:
                encoded += alphabet_list[ord(char) - 97]
            if encoded not in code_list:
                code_list.append(encoded)
        return len(code_list)