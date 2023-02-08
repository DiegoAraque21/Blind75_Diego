"""

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

class Solution(object):


    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #  create a result array that contains the indexes of the values that add up to the target
        result = []
        # map that contains keys as values of the array and values as the index of the value
        map_nums = {}

        # iterate through the array
        for i in range(len(nums)):
            # substract the current value from the target
            subsNum = target - nums[i]
            # if the substracted value is in the map, we found a result
            if subsNum in map_nums:
                result.append(map_nums[subsNum])
                result.append(i)
                return result
            # if the substracted value is not in the map, add the urrent value to the map
            map_nums[nums[i]] = i

        return result

Solution.twoSum(Solution, [2,7,11,15], 9)