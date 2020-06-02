"""Contiguous Array


Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.



Solution

"""
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if nums.count(0) == nums.count(1):
            return len(nums)
        
        counts = {}
        counts[0] = -1
        
        max_length = 0
        count = 0
        
        for i in range(0, len(nums)):
            if nums[i] == 0:
                count += -1
            else:
                count += 1
            print (count)
            if(count in counts):
                max_length = max(max_length, i - counts[count])
                print(max_length)
            else:
                counts[count] = i
        
        
        
        
        return max_length
        
        
      
            
        