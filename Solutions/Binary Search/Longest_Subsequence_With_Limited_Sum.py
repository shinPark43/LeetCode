class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        answer = []
        nums.sort()
        sum_hash_map = {}
        sum_of_num = 0

        for i in range(len(nums)):
            sum_of_num += nums[i]
            sum_hash_map[i] = sum_of_num


        for query in queries:
            subArray_length = 0

            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if sum_hash_map[mid] <= query:
                    subArray_length = mid + 1
                    low = mid + 1
                else:
                    high = mid - 1
            answer.append(subArray_length)
        return answer
