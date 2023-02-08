class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # create only one hashmap that will contain the count of both words
        anagram = {}

        # if they don't have the same size, we automatically return False
        if len(s) != len(t):
            return False

        # this makes it O(n), we will traverse the word once
        for i in range(len(s)):
            # if they are the same character and not in the anagram
            # make the counter of that letter bet 0
            # since +1 for bein in s and -1 for being in t
            if s[i] == t[i] and s[i] not in anagram:
                anagram[s[i]] = 0
            else:
                # +1 if it is found in the s word
                anagram[s[i]] = 1 + anagram.get(s[i], 0)
                # -1 if it is in the t word
                anagram[t[i]] = -1 + anagram.get(t[i], 0)

        # alphabet has max 26,
        # that's the max amount of times we will iterate in this process.
        for i in range(len(s)):
            if anagram[s[i]] != 0:
                print(False)
                return False
        
        print(True)
        return True


Solution.isAnagram(Solution, "dgqztusjuu", "dqugjzutsu")