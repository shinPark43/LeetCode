class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n = len(prices)
        ans = []
        for i in range(n):
            isFound = False
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    ans.append(prices[i] - prices[j])
                    isFound = True
                    break
            if not isFound:
                ans.append(prices[i])
        return ans
