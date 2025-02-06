class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        total_move = 0
        length = len(students)
        seats.sort()
        students.sort()

        for i in range(0, length):
            total_move += abs(students[i] - seats[i])
        return total_move                