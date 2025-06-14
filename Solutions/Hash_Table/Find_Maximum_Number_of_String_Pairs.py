class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        total_pair = 0
        reversed_set = set()

        for word in words:
            if word in reversed_set:
                total_pair += 1
            else:
                reversed_set.add(word[::-1])
        return total_pair
