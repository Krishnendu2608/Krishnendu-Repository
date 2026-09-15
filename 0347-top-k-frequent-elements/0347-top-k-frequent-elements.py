from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        if len(nums)==1:
            return nums
        frq=Counter()
        for i in nums:
            if i in frq:
                frq[i]+=1
            else:
                frq[i]=1
        highest=frq.most_common(k)
        result=[]
        for key,value in highest:
            result.append(key)
        return result

        
        
        