class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less_than = []
        equal = []
        greater_than =[]
        for num in nums:
            if num < pivot:
                less_than.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater_than.append(num)
        return less_than + equal + greater_than
