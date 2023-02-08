"""

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # value that will be returned
        result = nums[0]
        # length of the arr
        length = len(nums)

        if length == 1:
            return nums[0]

        # pointers for the start and the beginning
        i, j = 0,  length - 1

        while i <= j:
            if nums[i] < nums[j]:
                # check if the new number is lower than the current result
                # this is the final step and gives us the result we want
                result = min(result, nums[i])
                break

            # calculate the pivot
            pivot = (i+j) // 2
            # chech if the value in the pivot is lower than teh current min
            result = min(result, nums[pivot])

            # check what side of the array should we look for
            # in this step we are shrinking the array
            # if the number of the pivot is greater than the one on the left hand side
            # then we increase i
            if nums[pivot] >= nums[i]:
                # i pointer will now be pivot + 1, and we start looking in the right side
                i = pivot + 1
            else:
                # j pointer will now be pivot - 1, and we start looking in the left side
                j = pivot -1

        
        return result




            

print(Solution.findMin(Solution, [2,3,4,5,1]))