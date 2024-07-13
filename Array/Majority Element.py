"""
Summary of the approach:
This algorithm finds the majority element in a list by counting the occurrences of each number and 
keeping track of the number with the highest count.
"""
#Time: 0(n)
#Memory: 0(n)

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, maxCount = 0, 0

        for n in nums:
            count[n] = 1 + count.get(n,0)
            
            if count[n] > maxCount:
                res = n
            
            maxCount = max(count[n],maxCount)

        return res

            