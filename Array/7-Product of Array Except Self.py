"""
Link: https://leetcode.com/problems/product-of-array-except-self/description/

Summary of the approach:
Make two passes, first in-order, second in-reverse, to compute products then use the two result set. 
"""
#Time: 0(n)
#Memory: 0(1)

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

