class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        total = 0
        for i in hours:
            if i >= target:
                total += 1
        return total
