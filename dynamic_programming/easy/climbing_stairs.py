class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        one_step, two_steps = 1, 1

        # if we have 2 steps we just want to calculate
        # this one time.
        # If we have more than 2 we want to calculate it n-1 times
        for _ in range(n-1):
            temp = one_step
            one_step = one_step + two_steps
            two_steps = temp

        return one_step
