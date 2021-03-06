"""Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1


Solution: By Floyed cycle detection algorithm

"""
class Solution:
    
    def isHappy(self, n: int) -> bool:
        result = self.Total(n)
        temp = [result]
        while(result != 1):
            result = self.Total(result)
            if(result in temp):
                break
            temp.append(result)
  
        if(result == 1):
            return True
        else:
            return False
         
    def Total(self,n:int):
            rem = summ = 0
            while(n>0):
                rem = n%10
                summ = summ + rem**2
                n = int(n/10)
            return summ