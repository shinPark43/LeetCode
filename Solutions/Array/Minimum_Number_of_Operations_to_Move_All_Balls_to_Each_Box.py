class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        index_with_one = []
        answer = []

        for i in range(0, len(boxes)):
            if boxes[i] == '1':
                index_with_one.append(i)

        for i in range(0, len(boxes)):
            total_move = 0
            for j in index_with_one:
                if i != j:
                    total_move += abs(i - j)
            answer.append(total_move)

        return(answer)