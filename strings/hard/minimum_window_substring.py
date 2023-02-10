"""

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t == "":
            return ""
        # result min substring
        min_sub, len_sub = [-1, -1], float("infinity")
        # count of characters in t
        unique_chars = {}
        # count of characters in s
        window_chars = {}
        # fill the maps
        for char in t:
            unique_chars[char] = 1 + unique_chars.get(char, 0)
        
        # need and have variables, to keep an eye of what 
        # is happening on the current window
        need = len(unique_chars)
        have = 0

        # left pointer
        i = 0

        for j in range(len(s)):
            # add the char ocurrence to the map of the window
            window_chars[s[j]] = 1 + window_chars.get(s[j], 0)

            # increment the have value
            if s[j] in unique_chars and window_chars[s[j]] == unique_chars[s[j]]:
                have += 1
                        
            while have == need:
                # check if the current substring has the lowest length
                if (j + 1 - i) < len_sub:
                    min_sub = [i, j]
                    len_sub = j + 1 - i

                # getting rid of the element in the i pointer
                window_chars[s[i]] -= 1
                # if char being removed is in unique_chars
                # and it makes the ocurrence less than what we need to
                # then we substract 1 from have
                if s[i] in unique_chars and window_chars[s[i]] < unique_chars[s[i]]:
                    have -= 1
                i += 1

        if len_sub == float("infinity"):
            return ""
        else:
            return s[min_sub[0]: min_sub[1]+1]
                


print(Solution.minWindow(Solution, "aaaab", "ab"))