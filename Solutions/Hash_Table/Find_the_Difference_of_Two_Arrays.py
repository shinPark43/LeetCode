class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1_distinct = set(nums1)
        nums2_distinct = set(nums2)
        return [list(nums1_distinct - nums2_distinct), list(nums2_distinct - nums1_distinct)]
