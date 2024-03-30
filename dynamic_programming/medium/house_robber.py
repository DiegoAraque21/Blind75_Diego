class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        rob_all, curr_rob = 0, 0 

        for money in nums:

            # get the best option to rob
            temp_money = max(money + rob_all, curr_rob)

            # now rob_all the prev subarray is the last curr_rob
            rob_all = curr_rob

            # curr_rob is the max rob we can do
            curr_rob = temp_money

        return curr_rob

