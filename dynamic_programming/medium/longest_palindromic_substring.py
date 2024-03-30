"""

Given a string s, return the longest 
palindromic substring in s.

Example:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        longest_palindrome_indexes = []
        max_length = 0
        for i in range(len(s)):
            # check for odd palindromes, both pointers start in the same letter
            # expand to the right and left
            longest_palindrome_indexes, max_length = self.iterate(self, i, i, longest_palindrome_indexes, max_length, s)
            # check for even palindromes, one in the current letter an the 
            # other one to the left. We expand after that
            longest_palindrome_indexes, max_length = self.iterate(self, i, i + 1, longest_palindrome_indexes, max_length, s)
        
        return s[longest_palindrome_indexes[0]: longest_palindrome_indexes[1] + 1]
        
    def iterate(self, j, k, longest_palindrome_indexes, max_length, s):
        # if it is in range, and characters are equal
        while j >= 0 and k < len(s) and s[j] == s[k]:
            # if the length is bigger, change result values
            if (k - j + 1) > max_length:
                longest_palindrome_indexes = [j, k]
                max_length = k - j + 1
            # shift the pointers
            j -= 1
            k += 1
        return longest_palindrome_indexes, max_length

print(Solution.longestPalindrome(Solution, "babad"))