class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        total = 0
        hash_map = {}
        for word in words:
            hash_map[word] = hash_map.get(word, 0) + 1

        for word in words:
            reversed_word = word[::-1]
            if (
                reversed_word in hash_map and
                hash_map[word] > 0 and
                hash_map[reversed_word] > 0 and
                word != reversed_word
            ):
                total += 1
                hash_map[word] -= 1
                hash_map[reversed_word] -= 1

        return total
