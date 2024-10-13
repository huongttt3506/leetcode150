from typing import List
class BestTimeToBuyAndSellStock:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyPrice = prices[0]
        for p in prices:
            if p < buyPrice:
                buyPrice = p
            else:
                maxProfit = max(maxProfit, p - buyPrice)
        return maxProfit