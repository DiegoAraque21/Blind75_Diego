"""

Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # first of all we define 2 variables, for the min and max

        min_arr = 1
        max_arr = 1

        # result variable which will be returned
        result = nums[0]

        for n in nums:
            # ignore the 0 and reset values, multiplying by 0 is always 0
            # it does not matter if we reset it. Because we will keep track of the max value
            # in the result variable
            if n == 0:
                min_arr = 1
                max_arr = 1

            # temporary var, bcause if it is not calculated before hand
            # when we calculate the min, the maximum will not be the correct one
            max_temp = max_arr * n
            # get the max value
            max_arr = max(max_temp, n * min_arr, n)
            # get the min value
            min_arr = min(max_temp, n * min_arr, n)
            # get the result in comparison with the current max value
            result = max(result, max_arr)

        return result

            
        


print(Solution.maxProduct(Solution, [-1,5,4,0,3,5]))
