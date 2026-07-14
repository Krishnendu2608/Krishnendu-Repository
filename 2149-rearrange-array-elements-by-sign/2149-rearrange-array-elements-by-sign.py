class Solution(object):
    def rearrangeArray(self, nums):
        pos=[]
        neg=[]
        comb=[]
        for i in nums:
            if i >0:
                pos.append(i)
            elif i<0:
                neg.append(i)
        for j in range(len(pos)):
            comb.append(pos[j])
            comb.append(neg[j])
        return comb

        