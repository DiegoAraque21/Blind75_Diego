"""

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []

        if len(nums) < 2:
            return []

        # sort the input
        nums.sort()

        for i, num in enumerate(nums):
            # if we are not on the first element
            if i > 0 and nums[i-1] == num:
                # if the current num is the same as the previous one
                # we skip
                continue
            else:
                # two pointers, two itereate what's left of the array
                # one that starts after the current num we are in
                # the other one that the end of the array
                k = i + 1
                j = len(nums) - 1
                # iterate while the pointer of the start is smaller than the one of the end
                while k < j:
                    # make the sum
                    sum = nums[k] + nums[j] + num
                    # if it is 0
                    if sum == 0:
                        # append the result
                        result.append([num, nums[k], nums[j]])
                        # temp variable to keep track of prev num
                        tempLastNum = nums[k]
                        # shift the start pointer by 1
                        k += 1
                        # this loop is just in case we found a duplicate number,
                        # if that is the case we shift the start pointer by 1 more,
                        # and so one until we find a different number
                        while nums[k] == tempLastNum and k < j:
                            k += 1   
                    # if it is bigger than 0 we need to decrease the sum
                    # since we sorted the array we know that by decreasing 
                    # the end pointer we will get a smaller sum  
                    elif sum > 0:
                        j -= 1
                    # if it is smaller than 0, we do the complete opposite and 
                    # shift the start pointer to increase the value of the sum
                    elif sum < 0:
                        k += 1
        
        return result

print(Solution.threeSum(Solution, [-1,0,1,2,-1,-4]))








