class Solution(object):
    def maxSubarrayLength(self, nums, k):
        frq={}
        start=0
        longest=0
        for end in range(0,len(nums)):
            leading_el=nums[end]
            frq[leading_el]=frq.get(leading_el,0)+1
            while frq[leading_el]>k:
                trailing_el=nums[start]
                frq[trailing_el] -=1
                start+=1
            longest=max(end-start+1,longest)
        return longest
        