class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)

        answer1 = sum(num in set2 for num in nums1)
        answer2 = sum(num in set1 for num in nums2)
        return [answer1, answer2]
