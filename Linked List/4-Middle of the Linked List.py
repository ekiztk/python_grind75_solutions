"""
Link: https://leetcode.com/problems/middle-of-the-linked-list/description/

Summary of the approach:
Two pointers: slow, fast. 
"""
#Time: 0(n)
#Memory: 0(1)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow