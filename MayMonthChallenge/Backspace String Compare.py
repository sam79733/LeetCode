"""

Que::  Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.


Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".



"""
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
            return Solution.backSpace(S) == Solution.backSpace(T)
            
            
            
    def backSpace(s):
        lst=[];
        result = ''
        for x in s:
            if(x == '#'):
                if(len(lst) != 0):
                    lst.pop()
            else:
                lst.append(x)
        return result.join(lst);