class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        hash_map = {}
        kth_score = []

        for i in range(len(score)):
            kth_score.append(score[i][k])
            hash_map[score[i][k]] = i

        kth_score.sort(reverse=True)
        return [score[hash_map[sorted_score]] for sorted_score in kth_score]