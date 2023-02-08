"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example:

Input: s = "()[]{}"
Output: true

"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # create a stack for all the symbols we are getting
        symbols = []
        # map for closing and opening relation
        symbol_relation = {")": "(", "]": "[", "}": "{" }

        # If it is not even, then it at least one is not going to be closed
        if len(symbols) % 2 != 0:
            return False

        # iterate through the array
        for i in range(len(s)):
            # if it is an opening symbol, add it to the stack
            if s[i] in ["{", "[", "("]:
                symbols.append(s[i])
            # if it is a closing one and there are elements in the stack
            elif s[i] in symbol_relation and len(symbols) > 0:
                # check if it is the corresponding closing one
                if symbol_relation[s[i]] == symbols[-1]:
                    # eliminate it from the stack
                    symbols.pop()
                else:
                    # return false since it is not being closed correctly
                    return False
            else:
                # return false since it is not being closed correctly
                return False

        # if the stack is not empty return false, since a symbol wasn't closed
        if len(symbols) > 0:
            return False
        else:
            return True

print(Solution.isValid(Solution, "([)]"))


                


