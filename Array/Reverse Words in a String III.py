"""
Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

Summary of the approach:
1) Iterate through the string character by character.
2) When encountering a space or reaching the end of the string, reverse the word between the current left index (l) and the right index (r).
3) Move the left index (l) to the next word’s starting position.
4) Finally, join the reversed words to form the output string.
"""
#Time: 0(n)
#Memory: 0(n)

class Solution:
    def reverseWords(self, s:str) -> str:
        s = list(s)
        l = 0

        for r in range(len(s)):
            if s[r] == " " or r == len(s) - 1:
                temp_l,temp_r = l, r - 1

                if r == len(s) - 1:
                    temp_r = r
                
                while temp_l < temp_r:
                    s[temp_l], s[temp_r] = s[temp_r], s[temp_l]
                    temp_l += 1
                    temp_r -= 1
                
                l = r + 1

        return "".join(s)