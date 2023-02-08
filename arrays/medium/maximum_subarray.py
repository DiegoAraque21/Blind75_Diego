"""

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # maximum sum, this is the value that will be returned
        maxSum = nums[0]
        # current sum, so we can keep track. If this value is negative we reset it eventually
        curSum = 0
        # iterate through the array only one time
        for n in nums:
            # if the current sum value is negative, we reset it to 0.
            #  because of this we don't need to repeat operations and reduce the complexity
            if curSum < 0:
                curSum = 0
            
            # update the current sum value
            curSum += n
            # if the current sum is bigger than the maxSum that was previously appointed, then we reset the value
            maxSum = max(maxSum, curSum)
        
        return maxSum

print(Solution.maxSubArray(Solution, [-2,1,-3,4,-1,2,1,-5,4]))