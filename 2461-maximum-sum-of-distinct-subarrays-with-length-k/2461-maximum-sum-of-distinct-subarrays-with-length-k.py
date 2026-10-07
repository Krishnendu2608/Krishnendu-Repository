from collections import Counter
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        counts=Counter(nums[0:k])
        current_sum=sum(nums[0:k])
        max_sum=0
        if len(counts)==k:
            max_sum=current_sum
        for i in range(0,len(nums)-k):
            leading_char=nums[i+k]
            trailing_char=nums[i]
            current_sum+=leading_char-trailing_char
            counts[leading_char]+=1
            counts[trailing_char]-=1
            if counts[trailing_char]==0:
                del counts[trailing_char]
            if len(counts)==k:
                max_sum=max(current_sum,max_sum)
        return max_sum

        
        