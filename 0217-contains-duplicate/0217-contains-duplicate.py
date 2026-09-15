class Solution(object):
    def containsDuplicate(self, nums):
        frq={}
        for i in nums:
            if i in frq:
                frq[i] +=1
            else:
                frq[i]=1
        for key,values in frq.items():
            if values >1:
                return True
        return False
        