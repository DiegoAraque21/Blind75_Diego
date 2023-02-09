"""

Given a string s, find the length of the longest 
substring without repeating characters.

Example:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #left pointer
        i = 0
        # length that will be returned
        max_length = 0
        # alphabet hasmap, save indexes of the character
        alphabet = {}

        for j in range(len(s)):
            # check if the letter is in the hashmap
            # if it is lower than the current i
            # it is not in the current window
            # so we ignore it
            if s[j] in alphabet and alphabet[s[j]] >= i:
                # if it is, update the i pointer to the position of that letter
                # that position was saved in the hashmap
                i = alphabet[s[j]] + 1
            else:
                # update max length if necesarry
                max_length = max(max_length, j - i + 1)
            
            # add value to the alphabet
            alphabet[s[j]] = j

        return max_length

Solution.lengthOfLongestSubstring(Solution, "pwwkew")
                
                

