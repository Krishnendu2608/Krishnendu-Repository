class Solution(object):
    def findMaxAverage(self, nums, k):
        curr_sum=sum(nums[0:k])
        max_sum=curr_sum
        for i in range(0,len(nums)-k):
            curr_sum-=nums[i]
            curr_sum+=nums[i+k]
            max_sum=max(curr_sum,max_sum)
        return float(max_sum)/k
