class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        hash_map = {}
        key = key.replace(" ", "")

        ch = 'a'

        for char in key:
            if char not in hash_map:
                hash_map[char] = ch
                ch = chr(ord(ch) + 1)

        encoded_msg = ""

        for char in message:
            if char == ' ':
                encoded_msg += " "
            else:
                encoded_msg += hash_map[char]
        
        return encoded_msg