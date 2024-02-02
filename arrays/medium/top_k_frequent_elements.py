class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        occurences = {}
        occ_arr = [[] for i in range(len(nums)+1)]

        for num in nums:
            occurences[num] = 1 + occurences.get(num, 0)
        
        for num, occur in occurences.items():
            occ_arr[occur].append(num)

        res = []

        for i in range(len(occ_arr) - 1, 0, -1):
            for num in occ_arr[i]:
                res.append(num)
                if len(res) == k:
                    return res
