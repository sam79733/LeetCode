""" Majority Element
Solution
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2


Soultion-
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tempDict ={}
        for x in nums:
            if(x in tempDict):
                tempDict[x] = tempDict[x] + 1
            else:
                tempDict[x] = 1
                
        check = int(len(nums)/2)
                
        result = [x for x in tempDict if tempDict[x] > check]
        
        return result[0]