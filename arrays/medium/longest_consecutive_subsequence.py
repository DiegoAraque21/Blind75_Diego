class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numSet = set(nums)
        res = 0

        for num in nums:

            if (num - 1) not in numSet:

                seq_len = 1

                while (num+seq_len) in numSet:

                    seq_len += 1

                res = max(seq_len, res)

        return res