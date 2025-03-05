class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        frequency_map = {}
        length = len(A)
        common = 0
        C = []

        for i in range(0, length):
            if A[i] not in frequency_map:
                frequency_map[A[i]] = 1
            else:
                frequency_map[A[i]] += 1
                common += 1
            
            if B[i] not in frequency_map:
                frequency_map[B[i]] = 1
            else:
                frequency_map[B[i]] += 1
                common += 1
            C.append(common)
        return C
        