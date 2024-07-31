"""
Link: https://leetcode.com/problems/linked-list-cycle/description/

Summary of the approach:
Floyd's Tortoise and Hare 
dict to remember visited nodes; two pointers at different speeds, if they meet there is loop
"""
#Time: 0(n)
#Memory: 0(1)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
