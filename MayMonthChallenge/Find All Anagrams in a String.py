"""Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".



Solution:
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return None
        
        
        start_index = 0
        end_index = len(p)
        
        
        counter = 0
        ana_index = []
        
        check_lst = []
        
        while(counter < len(s)):
            
            if(s[start_index:end_index] in check_lst):
                 ana_index.append(start_index)
            else:
                if(self.isAnagram(s[start_index:end_index], p)):
                    check_lst.append(s[start_index:end_index])
                    ana_index.append(start_index)
            
            start_index = start_index + 1
            end_index = end_index + 1
            counter =  counter + 1
            
        
      
        return ana_index
  
        
    def isAnagram(self, s, p):
        if(len(s) != len(p)):
            return False
        
        if ''.join(sorted(s)) != ''.join(sorted(p)):
            return False
        
        
        return True
