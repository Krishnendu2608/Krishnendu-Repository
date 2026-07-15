class Solution(object):
    def containsDuplicate(self, nums):
        frq={}
        for i in nums:
            if i in frq:
                frq[i]+=1
            elif i not in frq:
                frq[i]=1
        for key,count in frq.items():
            if count>1:
                return True
        return False
               