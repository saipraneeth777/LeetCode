class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,profit=0,0
        for i in range(1,len(prices)):
            if(prices[l]<prices[i]):
                profit = max((prices[i]-prices[l]),profit)
            else:
                l = i
        return profit

        