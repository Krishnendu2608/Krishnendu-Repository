class Solution(object):
    def intersect(self, nums1, nums2):
        frq_nums1={}
        ans=[]
        for i in nums1:
            if i in frq_nums1:
                frq_nums1[i] +=1
            elif i not in frq_nums1:
                frq_nums1[i]=1
        for j in nums2:
            if j in frq_nums1 and frq_nums1[j]>0:
                ans.append(j)
                frq_nums1[j]-=1
        return ans
        