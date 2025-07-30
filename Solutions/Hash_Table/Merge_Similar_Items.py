class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        num_table = {}
        val_list = []
        ret = []
        for item in items1:
            num_table[item[0]] = item[1]
            val_list.append(item[0])
        for item in items2:
            if item[0] not in num_table:
                val_list.append(item[0])
                num_table[item[0]] = item[1]
            else:
                num_table[item[0]] += item[1]
        val_list.sort()
        return [[val, num_table[val]] for val in val_list]
