"""
Link: https://leetcode.com/problems/insert-interval/description/

Summary of the approach:
This approach inserts a new interval into a list of non-overlapping intervals by iterating through the list, merging overlapping intervals, 
and appending the new interval in the correct position.
"""
#Time: 0(n)
#Memory: 0(n)

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            #if end value of new interval is less than start value of current interval (insert the new before and return the result)
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            #if start value of new interval is greater than end value of current interval (insert the new after)
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            #if new interval is overlapping with current interval (merge two intervals)
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]

        #when the loop is done then add the new interval to the result
        res.append(newInterval)

        return res