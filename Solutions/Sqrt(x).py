class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low, high = 0, x

        if x > 1:
            high = high // 2

        while low <= high:
            mid = (low + high) // 2
            if mid**2 <= x < (mid+1)**2:
                return mid
            elif mid**2 < x:
                low = mid + 1
            else:
                high = mid - 1

        return -1 