class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        hash_map = {}
        for log in logs:
            if log[0] not in hash_map:
                hash_map[log[0]] = set()
                hash_map[log[0]].add(log[1])
            else:
                hash_map[log[0]].add(log[1])
        result = [0]*k
        for v in hash_map.values():
            result[len(v) - 1] += 1
        return result
