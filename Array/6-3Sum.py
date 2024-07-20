"""
Link: https://leetcode.com/problems/3sum/description/

Summary of the approach:
This algorithm finds all unique triplets in a sorted list that sum to zero by iterating through the list, skipping duplicates, 
and using a two-pointer technique to identify valid triplets while adjusting pointers to avoid duplicates.
"""
#Time: 0(nlogn) + O(n^2) = O(n^2)
#Memory: 0(n) or O(1) (depends on sorting algorithm)

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            #if the same value with the previous then continue
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1

            # modify two sum 2 problem solution
            while l < r: 
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -=1
                elif threeSum < 0:
                    l +=1
                else:
                    res.append([a, nums[l], nums[r]])
                    # we have to update pointers still
                    l +=1
                    # if the left index value same with the previous then move to the next
                    while nums[l] == nums[l-1] and l < r:
                        l +=1
        return res
            


        