class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element_sum = 0
        digit_sum = 0

        for num in nums:
            element_sum += num

            while num > 0: 
                digit_sum += (num % 10)
                num = num // 10

        return abs(element_sum - digit_sum) 
