from pyparsing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_id = max_id = 0
        profit = -1
        for ind in range(len(prices)):
            if prices[ind] < prices[min_id]:
                min_id = max_id = ind
            elif prices[ind] > prices[max_id]:
                max_id = ind
            current_profit = prices[max_id] - prices[min_id]
            if current_profit > profit:
                profit = current_profit
        
        return profit
