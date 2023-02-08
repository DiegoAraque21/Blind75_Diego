""""

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # result array
        res = [1] * len(nums)

        # get the prefixes on the result array
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            # update the prefix [1,2,3]
            # prefixes = [1,1,2]
            prefix = prefix * nums[i]

        # get the suffixes, and multiply them to the already filled
        # result array. After doing this multiplication we solve the problem
        # traverse the array in a reverse order
        suffix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res



         