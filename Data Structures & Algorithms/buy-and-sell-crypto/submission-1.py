class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        price = 0
        # take the maximum between the profit and a calculated price

        l = 0
        r = 1
        n = len(prices) 

        while r > l and r < n: 

            # cheaper price to buy
            if prices[r] > prices[l]:
                price = prices[r] - prices[l]          
                profit = max(profit, price)
            elif prices[r] < prices[l]:
                l = r
            r += 1
        
        return profit