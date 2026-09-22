class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        frq={}
        for i in arr:
            if i in frq:
                frq[i]+=1
            else:
                frq[i]=1
        ls=[]
        for key,value in frq.items():
            ls.append(value)
        ls.sort()
        unique_count=len(ls)
        for j in ls:
            if k>=j:
                k=k-j
                unique_count -=1
            else:
                break
        return unique_count

        