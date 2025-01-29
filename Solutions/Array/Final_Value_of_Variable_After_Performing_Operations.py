class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        num = 0
        for i in operations:
            if i.find("++") != -1:
                num += 1
            elif i.find("--") != -1:
                num -= 1
        return num
