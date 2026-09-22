class Solution(object):
    def minOperations(self, nums):
        frq={}
        total=0
        for i in nums:
            if i in frq:
                frq[i]+=1
            else:
                frq[i]=1
        for key,value in frq.items():
            if value<2:
                return -1
            elif value%3==0:
                steps=value//3
                total+=steps
            else:
                steps=(value//3)+1
                total+=steps
        return total

        