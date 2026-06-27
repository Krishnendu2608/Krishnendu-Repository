class Solution(object):
    def findLonely(self, nums):
        frq_map={}
        lonely=[]
        for i in nums:
            if i in frq_map:
                frq_map[i] +=1
            else:
                frq_map[i]=1
        for ele,frq in frq_map.items():
            if frq==1 and (ele-1) not in frq_map and(ele+1) not in frq_map:
                lonely.append(ele)
        return lonely
                
            

        