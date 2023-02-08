"""

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # left and right pointer
        i = 0
        j = len(s) - 1
        # iterate the string
        while i < j:
            # if both are alphanum
            if self.is_alhpa_numeric(self, s[i]) and self.is_alhpa_numeric(self, s[j]):
                # if they are equal by being lowercase
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
            # if both are not alphanumerical 
            elif not self.is_alhpa_numeric(self, s[i]) and not self.is_alhpa_numeric(self, s[j]):
                j -= 1
                i += 1
            # if left pointer is alphanum decrement the right one 
            elif self.is_alhpa_numeric(self, s[i]):
                j -= 1
            # if right pointer is alphanum increment the left one 
            elif self.is_alhpa_numeric(self, s[j]):
                i += 1
        
        return True

    # I can also use isalnum(), but this solution is just in 
    # case the interviewer wants me to make my one function
    def is_alhpa_numeric(self, char):
        return ("a" <= char.lower() <= "z" or "0" <= char <= "9" )

print(Solution.isPalindrome(Solution, "A man, a plan, a canal: Panama"))

