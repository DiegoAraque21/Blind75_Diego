"""

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        length = len(nums)

        i, j = 0, length - 1

        result = -1

        while i <= j:

            # get the pivot to always be the half of the new array
            pivot = (i + j) // 2

            # when we find the target we return it
            if nums[pivot] == target:
                result = pivot
                break
            
            # check if the bottom one is sorted
            if nums[pivot] >= nums[i]:
                # if it is and the target is in range, reduce the j pointer
                if target < nums[pivot] and target >= nums[i]:
                    j = pivot - 1
                # if not, i = one more than the pivot
                else:
                    i = pivot + 1
            # if it is not sorted
            else:
                # check if it is in the range, i = one more than the pivot
                if target > nums[pivot] and target <= nums[j]:
                    i = pivot + 1
                # if not, reduce j
                else:
                    j = pivot - 1

        return result

        
print(Solution.search(Solution,[5,1,2,3,4], 1))