class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in grid:
            n = len(i)
            for j in range(n):
                if i[j] < 0:
                    count += (n - j)
                    break
        return count
