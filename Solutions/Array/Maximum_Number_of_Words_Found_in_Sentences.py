class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        largest_count = 0

        for i in sentences:
            word_count = i.count(' ') + 1
            if word_count > largest_count:
                largest_count = word_count
        return largest_count