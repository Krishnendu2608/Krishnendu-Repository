class Solution(object):
    def maximumWealth(self, accounts):
        richest=0
        for i in accounts:
            total=0
            for j in i:
                total=total+j
            if total > richest:
                richest=total
        return richest
        