class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """

        distinct_list = []
        for string in arr:
            if string not in distinct_list:
                distinct_list.append(string)

        distinct_string = []

        for string in distinct_list:
            if arr.count(string) == 1:
                distinct_string.append(string)
        
        if k > len(distinct_string):
            return ""
        else:
            return distinct_string[k-1]
