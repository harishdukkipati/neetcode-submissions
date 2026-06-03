#Understand
# We need to find the minimum amount of coins to make up an amount

#Plan 
# create a dp array with length of amount + 1 to float('inf')
# set the first element in dp element to 0 because it takes 0 coins to get to cost of 0 
# do for loop from 1 to amount + 1 
# for c in coins 
# dp[i] = min(dp[i-c] + 1, dp[i])
# if dp[-1] is float('inf') -> coudln't reach that amount, return -1
# return dp[-1]
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i-c] + 1, dp[i])
        
        if dp[-1] == float('inf'):
            return -1
        
        return dp[-1]