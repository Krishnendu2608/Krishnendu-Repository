class Solution(object):
    def findLucky(self, arr):
        frq={}
        for i in arr:
            if i in frq:
                frq[i] +=1
            elif i not in frq:
                frq[i]=1
        lucky=[]
        for key,count in frq.items():
            if key==count:
                lucky.append(key)
        if len(lucky)==0:
            return -1
        elif len(lucky)==1:
            return lucky[0]
        elif len(lucky)>1:
            return max(lucky)
            

        