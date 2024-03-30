class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        # cache
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        # bottom up
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                # check if word exists
                if i + len(w) <= len(s) and w == s[i:i+len(w)]:
                    # if it does, change the cash to the one of the previous completed_word
                    # if there is no prev completed words
                    # then it will always be false
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]