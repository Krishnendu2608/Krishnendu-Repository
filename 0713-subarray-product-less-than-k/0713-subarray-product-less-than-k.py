class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        start=0
        window_mul=1
        count=0
        for end in range(0,len(nums)):
            window_mul *=nums[end]
            while window_mul>=k and start<=end:
                window_mul /=nums[start]
                start+=1
            count+=end-start+1
        return count

        