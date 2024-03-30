"""

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

"""
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # hashmap, key will be sorted word. It's default since all of the values are going to be lists
        grouped_anagrams = defaultdict(list)

        # go through the array one O(n), n being the length of strs
        for i in range(len(strs)):
            # sort the word in question. klog(k), k being the size of the string
            # it will be different for every single one
            sorted_word = "".join(sorted(strs[i]))
            # append it to the dictionary
            grouped_anagrams[sorted_word].append(strs[i])

        # return each one of the anagrams grouped
        return grouped_anagrams.values()
    
class Solution2(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # minor optimization since complexity is now 0(m*n) instead of O(m*n*logn)
        
        result = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for l in word:
                count[ord(l) - ord("a")] += 1
            
            result[tuple(count)].append(word)
        
        return result.values()


print(Solution.groupAnagrams(Solution, [""]))



        
