class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        largest_num = 0
        for i in candies:
            if i >= largest_num:
                largest_num = i
        for i in candies:
            if i + extraCandies >= largest_num:
                result.append(True)
            else:
                result.append(False)
        return result