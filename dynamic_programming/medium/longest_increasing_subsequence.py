class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # all longest at the beginning is 1
        dp = [1] * (len(nums))

        # bottom-up
        for i in range(len(nums)-1, -1, -1):
            # check all numbers of remaining sub array
            for j in range(i+1, len(nums)):
                # if less than one of the sub array
                # update the quantity if needed
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        # return the maximum in the cache
        return max(dp)