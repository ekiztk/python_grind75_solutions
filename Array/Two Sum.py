"""
Summary of the approach:
The algorithm uses a dictionary to track indices of previously seen numbers and 
checks if the complement of the current number (to reach the target) exists in the dictionary, returning the indices if found.
"""
#Time: 0(n)
#Memory: 0(n)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i,n in enumerate(nums):
            diff = target - n

            if diff in prevMap:
                return [prevMap[diff],i]
            
            prevMap[n] = i

        return