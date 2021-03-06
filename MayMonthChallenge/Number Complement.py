"""Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
 

Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 
 


Solution:
"""
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        res=0
        lst = []
        while(num > 0):
            rem = num % 2 
            num = int(num/2)
            lst.append(rem)
       
        
        
        resultLst =  [0 if(x==1) else 1 for x in lst]
        print(resultLst)
        result = 0
        pw = 0
        for x in resultLst:
            result =  result + x * pow(2, pw)
            pw = pw + 1
            
        return result
        