class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        def maxsum(target):
            left=0
            right=len(nums)-1
            count=0
            while left<right:
                if nums[right]+nums[left]<=target:
                    count+=right-left
                    left+=1
                else:
                    right=right-1
                    
            return count
        return maxsum(upper)-maxsum(lower-1)
        