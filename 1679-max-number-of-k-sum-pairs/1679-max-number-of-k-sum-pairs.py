class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        pairs=0
        left=0
        right=len(nums)-1
        while left < right:
            current_sum=nums[left] + nums[right]
            if current_sum==k:
                left +=1
                right -=1
                pairs=pairs+1
            elif current_sum<k:
                left +=1
            elif current_sum >k:
                right=right-1
        return pairs
        

        