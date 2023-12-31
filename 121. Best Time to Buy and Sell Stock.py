


# Input: prices = [7,1,5,3,6,4]
# Output: 5
# buy at 1 and sell at 6 6-1 =  5 is maximum profit




class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables to keep track of the minimum price and maximum profit
        min_price = prices[0]
        max_profit = 0
        
        # Iterate through the prices starting from the second element
        for price in prices[1:]:
            # Update the maximum profit by comparing the current profit with the previous maximum
            max_profit = max(max_profit, price - min_price)
            
            # Update the minimum price if the current price is smaller
            min_price = min(min_price, price)
            
        # Return the final maximum profit
        return max_profit




# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104
