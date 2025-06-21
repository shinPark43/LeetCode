class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        total = 0
        for passenger in details:
            if int(passenger[11:13]) > 60:
                total += 1
        return total   
