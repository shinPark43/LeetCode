class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        balls = 0
        operations = 0
        length = len(boxes)
        answer = [0]*length

        # Left sweep
        for i in range(0, length):
            if boxes[i] == '1':
                balls += 1
            answer[i] += operations
            operations += balls

        balls = 0
        operations = 0
        # Right sweep
        for i in range(length - 1, -1, -1):
            if boxes[i] == '1':
                balls += 1
            answer[i] += operations
            operations += balls
        
        return(answer)