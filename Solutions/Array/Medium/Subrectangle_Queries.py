class SubrectangleQueries(object):

    def __init__(self, rectangle):
        """
        :type rectangle: List[List[int]]
        """
        self.rectangle = rectangle
        self.num_column = len(rectangle[0])
        

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :type newValue: int
        :rtype: None
        """
        flat_rectangle = [x for sublist in self.rectangle for x in sublist]

        start = row1 * self.num_column + col1
        end = row2 * self.num_column + col2

        for i in range(start, end + 1):
            flat_rectangle[i] = newValue
        
        self.rectangle = [flat_rectangle[i:i + self.num_column] for i in range(self.num_column)]

    def getValue(self, row, col):
        """
        :type row: int
        :type col: int
        :rtype: int
        """
        num = self.rectangle[row][col]
        return num
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)