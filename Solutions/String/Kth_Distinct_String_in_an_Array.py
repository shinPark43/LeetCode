class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """

        distinct_hashmap = {}
        for string in arr:
            if string not in distinct_hashmap:
                distinct_hashmap[string] = 1
            else:
                distinct_hashmap[string] += 1

        distinct_string = []

        for string in arr:
            if distinct_hashmap[string] == 1:
                distinct_string.append(string)
        
        if k > len(distinct_string):
            return ""
        else:
            return distinct_string[k-1]
