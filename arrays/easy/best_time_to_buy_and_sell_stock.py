"""

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0 # buy
        j = 1 # sell
        max_profit = 0 # max prfit you get
        # iterate the prices array with the sell pointer
        while j < len(prices):
            # calculate the current profit
            profit = prices[j] - prices[i]
            # check if the price selected is the minimum one to buy
            if prices[i] < prices[j]:
                # get the max profit
                if max_profit < profit:
                    max_profit = profit
            # if the minimum is on the sell pointer, update the buy pointer
            else:
                i = j
            # always update the sell pointer
            j += 1

        return max_profit

Solution.maxProfit(Solution, [7,1,5,3,6,4])

