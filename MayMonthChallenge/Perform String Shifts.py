"""Perform String Shifts


You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.


Example 1:

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"


Example 2:

Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"




"""
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        for x in shift:
            direction =  x[0]
            amount =  x[1]
            s = self.shiftChar(list(s), direction, amount)
        return s
    
    
    def shiftChar(self, lst, direction, amount):
        x = direction
        a = amount
        if(x==1):
            for x in range(a):
                c = lst[len(lst)-1]
                lst.pop(len(lst)-1)
                lst.insert(0,c)
            return "".join(lst)
        if(x==0):
            for x in range(a):
                c = lst[0]
                lst.pop(0)
                lst.append(c)
            return "".join(lst)