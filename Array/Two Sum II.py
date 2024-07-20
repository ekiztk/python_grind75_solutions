"""
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

Summary of the approach:
-
"""
#Time: 0(n)
#Memory: 0(1)

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum > target:
                r = r-1
            elif sum < target:
                l = l+1
            else:
                return [l+1, r+1]
            
        return []