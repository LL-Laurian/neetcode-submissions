class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max(prices [b] - prices[a]) where b>a
        # for each item , max(whatever on right) - item
        if prices == []:
            return 0

        curr_min = prices[0]
        max_profit = 0
        for price in prices:
            max_profit = max(max_profit, price - curr_min)
            curr_min = min(price, curr_min)

        return max_profit