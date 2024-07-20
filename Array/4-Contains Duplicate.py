"""
Link: https://leetcode.com/problems/contains-duplicate/description/

Summary of the approach:
This approach checks for duplicates in a list by using a hash set to track seen numbers, 
returning `True` if a duplicate is found during iteration.
"""
#Time: 0(n)
#Memory: 0(n)

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numHashset = set()

        for n in nums:
            if n in numHashset:
                return True
            
            numHashset.add(n)
        
        return False
            