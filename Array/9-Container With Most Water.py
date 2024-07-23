"""
Link: https://leetcode.com/problems/container-with-most-water/description/

Summary of the approach:
Shrinking window, left/right initially at endpoints, shift the pointer with min height
"""
#Time: 0(n)
#Memory: 0(1)

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        res = 0

        # if we use l and r, consider using while instead of for loop
        while l < r:
            area = (r-l) * min(height[l],height[r])
            res = max(res,area)
            
            if height[l] < height[r]:
                l +=1
            # elif height[l] > height[r]:
            #     r -=1
            else:
                r -=1
        return res