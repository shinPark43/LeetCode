class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        total = 0
        for i in words:
            is_consistent = True
            for j in i:
                if not j in allowed:
                    is_consistent = False
                    break
            if is_consistent == True:
                total += 1
        return total