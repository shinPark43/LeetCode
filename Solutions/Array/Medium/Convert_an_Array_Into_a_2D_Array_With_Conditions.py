class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        sort_list = [[] for i in range(length)]
        largest_count = 0

        for i in nums:
            sort_list[i - 1].append(i)
            if (len(sort_list[i - 1])) > largest_count:
                largest_count = len(sort_list[i - 1]) 

        result = [[] for i in range(largest_count)]

        for i in sort_list:
            if i:
                for j in result:
                    if i:
                        j.append(i[0])
                        i.pop()
                    else:
                        break
        return result
            
                