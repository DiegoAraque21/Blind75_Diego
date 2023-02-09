"""

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

"""

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # sliding window pointers
        i = 0
        # repetition of letters hash map
        alphabet = {}
        # max length of a substring
        max_length = 0

        # we will traverse through the array once
        for j in range(len(s)):
            # increment the ocurrence of the letter in the j pointer
            alphabet[s[j]] = 1 + alphabet.get(s[j], 0)

            # get the max ocurrence. 0(26) since we will always have 
            vals = alphabet.values()    
            max_ocurrence = max(vals)

            # while it is not on range, decrement
            # this does not make it O(nˆ2), because 
            # this loop is not called in every single iteration
            while (j - i + 1 - max_ocurrence) > k:
                # it will always exits in the hasmap, hence no get function
                alphabet[s[i]] -= 1
                # increment the start pointer
                i += 1

            # change max length
            max_length = max(max_length, j-i+1)

        print(max_length)
        return max_length

Solution.characterReplacement(Solution, "AABABBA", 1)
                


