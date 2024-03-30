class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # cache
        dp = [0 for _ in range(len(s)+1)]
        # last element will have always one
        dp[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            # no letter has index 0
            if s[i] == "0":
                dp[i] = 0
            # all others make them have the prev
            # reads
            else:
                dp[i] = dp[i + 1]
            
            # conditional to check double digit, if
            # it's a double digit then sum cache + 2
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2]
        
        return dp[0]
