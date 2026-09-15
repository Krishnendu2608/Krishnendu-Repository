class Solution(object):
    def findDuplicate(self, nums):
        frq={}
        for i in nums:
            if i in frq:
                frq[i]+=1
            else:
                frq[i]=1
        for key,value in frq.items():
            if value>1:
                return key
        return -1
        