class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        hold = [0] * len(prices)
        not_hold = [0] * len(prices)
        hold[0] = -prices[0]

        for i in range(1, len(prices)):
            not_hold[i] = max(not_hold[i-1], hold[i-1]+prices[i])
            hold[i] = max(hold[i-1], not_hold[i-2]-prices[i] if i > 1 else -prices[i])
        
        return not_hold[-1]
