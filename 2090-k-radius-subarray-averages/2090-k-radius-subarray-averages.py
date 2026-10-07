class Solution(object):
    def getAverages(self, nums, k):
        n=len(nums)
        result=[-1]*n
        window_size=(2*k)+1
        if window_size>n:
            return result
        current_sum=sum(nums[:window_size])
        result[k]=current_sum//window_size
        for i in range(k+1,n-k):
            current_sum+=nums[i+k]-nums[i-k-1]
            result[i]=current_sum//window_size
        return result
