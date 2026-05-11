class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        profit = 0

        while buy < sell and sell in range(0, len(prices)):
            if prices[buy] < prices[sell]:
                profit = max(profit, prices[sell] - prices[buy])
                sell += 1
            else:
                buy += 1
                sell = buy + 1 
        return profit

