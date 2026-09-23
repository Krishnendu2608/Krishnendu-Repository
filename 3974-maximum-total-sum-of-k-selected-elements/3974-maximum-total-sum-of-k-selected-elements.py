class Solution(object):
    def maxSum(self, nums, k, mul):
        nums.sort(reverse=True)
        total=0
        for i in range(k):
            gain=nums[i]*max(mul,1)
            mul-=1
            total+=gain
        return total