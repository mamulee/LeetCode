class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        answer = 0
        for price in prices[1:]:
            minp = min(minp, price)
            answer = max(answer, price - minp)
        return answer