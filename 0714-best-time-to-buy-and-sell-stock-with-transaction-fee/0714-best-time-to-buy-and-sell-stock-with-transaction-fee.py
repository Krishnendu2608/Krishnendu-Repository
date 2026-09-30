class Solution(object):
    def maxProfit(self, prices, fee):
        free=0
        hold=-prices[0]
        for i in range(1,len(prices)):
            prev_free=free
            free=max(free,hold+prices[i]-fee)
            hold=max(hold,prev_free-prices[i])
        return free