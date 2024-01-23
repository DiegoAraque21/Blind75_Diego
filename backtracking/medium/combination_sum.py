class Solution(object):

    def __init__(self):
        self.res = []

    def dfs(self, i, curr_comb, total_sum, target, candidates):

        # if target is reached add to result
        if total_sum == target:
            copy_comb = list(curr_comb)
            self.res.append(copy_comb)
            return
        # if target is exceeded or no more numbers to expand the decision tree
        # end algorithm
        if total_sum > target or i >= len(candidates):
            return
        
        # add new element to decision tree
        curr_comb.append(candidates[i])
        # recursive call for the left side of the tree,
        # only contains number repetitions, it stops until goal is reached
        # or exceeded or no more numbers to add. We don't add previous numbers from before
        self.dfs(i, curr_comb, total_sum + candidates[i], target, candidates)
        # expand right side, so we eliminate last element added to the combination
        #         [2,2]
        #  [2,2,2]     [2,2,3]
        curr_comb.pop()
        # recursive call for the right side. We increase i so we don't add
        # the number from before
        self.dfs(i+1, curr_comb, total_sum, target, candidates)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
    
        self.dfs(0, [], 0, target, candidates)
        return self.res
        