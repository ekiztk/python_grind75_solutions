"""
Link: https://leetcode.com/problems/valid-parentheses/description/

Summary of the approach:
-
"""
#Time: 0(n)
#Memory: 0(n) #using stack

from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")":"(" , "]":"[", "}":"{"}

        for c in s:
            # if it is closing character
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False   

