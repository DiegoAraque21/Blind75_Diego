class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]
        
        def robbing(houses):

            rob_all, curr_rob = 0, 0

            for money in houses:

                temp_money = max(rob_all + money, curr_rob)

                rob_all = curr_rob

                curr_rob = temp_money

            return curr_rob

        first_robbery, second_robbery = robbing(nums[:-1]), robbing(nums[1:])
        
        return max(first_robbery, second_robbery)

        