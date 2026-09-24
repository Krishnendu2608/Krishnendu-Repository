class Solution(object):
    def twoCitySchedCost(self, costs):
        costs.sort(key=lambda i:i[1]-i[0])
        total_cost=0
        n=len(costs)//2
        for j in range(len(costs)):
            if j<n:
                total_cost+=(costs[j][1])
            else:
                total_cost+=(costs[j][0])
        return total_cost
        