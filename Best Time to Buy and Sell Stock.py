class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        
        high = prices[len(prices)-1]
        res = 0
        
        for i in prices[::-1]:
            if high - i > res:
                res = high - i
            if i > high:
                high = i
        
        return res
        