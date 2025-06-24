import math

class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        answer = []

        for circle in queries:
            total = 0
            for point in points:
                distance = math.sqrt((((point[0] - circle[0])**2) + ((point[1] - circle[1])**2)))
                if distance <= circle[2]:
                    total += 1
            answer.append(total)
        return answer
