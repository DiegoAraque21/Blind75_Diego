"""

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

"""

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        num_palindromes = 0

        # itereta once through the string
        for i in range(len(s)):
            # odd: pointers start in the same position, and expand
            l, r = i, i
            num_palindromes = self.is_palindrome(self, l, r, num_palindromes, s)
             # even: left pointer on i and right pointer on the the current pos + 1
            l, r = i, i + 1
            num_palindromes = self.is_palindrome(self, l, r, num_palindromes, s)

        return num_palindromes

    def is_palindrome(self, l, r, num_palindromes, s):
        # if it's in range, and they are palindromes
        # then we accept the condition
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # add 1 to the counter of palindromes
            num_palindromes += 1

            # expand pointers
            l-=1
            r+=1

        return num_palindromes

        


print(Solution.countSubstrings(Solution, "abc"))