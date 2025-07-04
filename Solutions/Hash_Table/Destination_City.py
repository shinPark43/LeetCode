class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        # start_city = set()
        # destination = set()
        # for path in paths:
        #     start_city.add(path[0])
        #     destination.add(path[1])
        # return (destination - start_city).pop()
        path_table = {}
        for path in paths:
            path_table[path[0]] = path[1]
        destination = paths[0][1]
        while destination in path_table:
            destination = path_table[destination]
        return destination
