class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        hash_table = {}

        for i in range(len(names)):
            hash_table[heights[i]] = names[i]

        heights.sort(reverse=True)
        return [hash_table[i] for i in heights]
