class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        # Create nested list to sort people out by group size
        n = len(groupSizes)
        sorted_list = [[] for i in range(n + 1)]
        result = []

        # Looping through groupSizes list to sort people out by group size
        for i in range(0, n):
            sorted_list[groupSizes[i]].append(i)
        
        # Slicing the sorted groups by their group size and appending to result list
        for i in range(0, n+1):
            if sorted_list[i]:
                start_idx = 0
                length = len(sorted_list[i])
                for j in range(0, length, i):
                    result.append(sorted_list[i][j:j+i])
        return result