class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        where_to_look = 0
        if ruleKey == "color":
            where_to_look = 1
        elif ruleKey == "name":
            where_to_look = 2

        total = 0
        for i in items:
            if ruleValue == i[where_to_look]:
                total += 1
            
        return total
