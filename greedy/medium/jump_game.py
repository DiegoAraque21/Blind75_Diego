class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            print(i, nums[i], goal)
            if i + nums[i] >= goal:
                goal = i

        # if the lst index can be reached, then
        # we can reach the last element of the array
        if goal == 0:
            return True
        else:
            return False
            

