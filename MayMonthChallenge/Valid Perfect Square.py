""" Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false


Solution:


"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        val = num
        maxx = num
        while(True):
            x = int(val/2)
            if( x * x== num):
                return True
            if(x * x < num):
                for x in range(maxx+1):
                    if(x*x == num):
                        return True
                return False
            val =  x
            maxx  = x
        