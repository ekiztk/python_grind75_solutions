"""
Link: https://leetcode.com/problems/ransom-note/description/

Summary of the approach:
-
"""
#Time: 0(m + n)
#Memory: 0(1) #because there are 26 letters only

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}

        for c in magazine:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        
        for c in ransomNote:
            if c not in counter:
                return False
            elif counter[c] == 1:
                del counter[c]
            else:
                counter[c] -= 1
        
        return True
