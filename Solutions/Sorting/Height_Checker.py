class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        ct = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                ct += 1
        return ct
