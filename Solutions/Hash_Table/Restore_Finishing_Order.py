class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        friends_set = set(friends)
        result = []
        for ids in order:
            if ids in friends_set:
                result.append(ids)
        return result
