class Solution(object):
    def maximumHappinessSum(self, nums, k):
        nums.sort(reverse=True)
        total=0
        for i in range(k):
            gain=max(nums[i]-i,0)
            total+=gain
        return total


        