"""Permutation in String



Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.


Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False


Hint- Sliding window

from collections import Counter
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        start_index = 0
        end_index = len(s1)
        
        while (start_index < len(s2)):
            sub = s2[start_index:end_index]
            if(Counter(sub) ==  Counter(s1)):
                return True
            start_index = start_index + 1
            end_index = start_index + len(s1)
