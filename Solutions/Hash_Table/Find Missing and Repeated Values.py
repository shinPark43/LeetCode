class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        hash_table = {}
        ans = []
        for i in grid:
            for j in i:
                if j not in hash_table:
                    hash_table[j] = 1
                else:
                    ans.append(j)
        for i in range(1, n*n + 1):
            if i not in hash_table:
                ans.append(i)
        return ans
