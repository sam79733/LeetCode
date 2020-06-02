"""Given an integer array arr, count element x such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.

 

Example 1:

Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.









"""
class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        for x in arr:
            if((x+1) in arr):
                count = count + 1
        return count