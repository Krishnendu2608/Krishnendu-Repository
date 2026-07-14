class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        target=(n/2)
        frq={}
        for i in nums:
            if i not in frq:
                frq[i]=1
            elif i in frq:
                frq[i] +=1
        for key, count in frq.items():
            if count>target:
                return key
            
        