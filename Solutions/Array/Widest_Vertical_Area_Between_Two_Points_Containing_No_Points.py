class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        largest_width = 0

        x_coordinates = [coor[0] for coor in points]
        x_coordinates.sort()

        for i in range(1, len(x_coordinates)):
            width = x_coordinates[i] - x_coordinates[i - 1]
            if width > largest_width:
                largest_width = width
        
        return largest_width