class Solution(object):
    def withinDaysChecker(self, weights, leastCapacity):
        day = 1
        cur_amount = 0
        for weight in weights:
            if cur_amount + weight > leastCapacity:
                day +=1
                cur_amount = weight
            else:
                cur_amount += weight
        return day

    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        minWeight = max(weights)
        maxWeight = sum(weights)

        result = maxWeight

        while minWeight <= maxWeight:
            mid = (minWeight + maxWeight) // 2
            leastCapacity = self.withinDaysChecker(weights, mid)
            if leastCapacity <= days:
                result = mid
                maxWeight = mid - 1
            else:
                minWeight = mid + 1
        return result
