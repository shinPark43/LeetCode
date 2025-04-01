class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_max = []
        column_max = []

        for block in grid:
            tallest = 0
            for height in block:
                if height > tallest:
                    tallest = height
            row_max.append(tallest)
        
        i = 0
        tallest = 0

        for j in range(len(grid)):
            while i != len(grid):
                if grid[i][j] > tallest:
                    tallest = grid[i][j]
                i += 1
            column_max.append(tallest)
            i = 0
            tallest = 0

        total = 0

        for i in range(len(grid)):
            for j in range(len(grid)):
                height = min(row_max[i], column_max[j])
                if grid[i][j] < height:
                    total += (height - grid[i][j])
        return total