"""
Purpose: Buy low sell high

Summary of the approach:
The algorithm finds the maximum profit by iterating through prices with two pointers, 
updating the maximum profit whenever a higher selling price is found after a lower buying price.
"""
#Time: 0(n)
#Memory: 0(1)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left=buy, right=sell
        maxP = 0

        while r < len(prices):
            #profitable ?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            
            r +=1
        return maxP
