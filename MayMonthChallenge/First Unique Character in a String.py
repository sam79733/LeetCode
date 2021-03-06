"""  First Unique Character in a String
Solution
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.


Solution
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        tempDict= {}
        for x in s:            
                if(x not in tempDict):
                    tempDict[x] = 1
                else:
                    tempDict[x] = tempDict[x] + 1
                    
        counter = 0
        for x in s:
            if(tempDict[x] == 1):
                return counter
            counter = counter + 1
        return -1
     

        