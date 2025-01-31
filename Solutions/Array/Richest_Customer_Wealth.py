class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        largest = 0
        for i in accounts:
            temp = 0
            for j in i:
                temp += j
            if temp > largest:
                largest = temp
        return largest
