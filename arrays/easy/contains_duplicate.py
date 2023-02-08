"""

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example:
Input: nums = [1,2,3,1]
Output: true

"""

class Solution(object):
    def containsDuplicate(self, nums):
        # hash map that will let us iterate only once through the array
        map = {}
        # iterate through the array
        for i in range(len(nums)):
            # if the current value is in the map, we found a duplicate
            if nums[i] in map:
                print("True")
                return True
            # if the current value is not in the map, add it to the map
            else:
                map[nums[i]] = 1
        print("False")
        return False

Solution.containsDuplicate(Solution, [1,2])