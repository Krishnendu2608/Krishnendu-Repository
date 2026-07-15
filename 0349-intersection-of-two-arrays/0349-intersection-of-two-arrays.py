class Solution(object):
    def intersection(self, nums1, nums2):
        s_nums1=set(nums1)
        s_nums2=set(nums2)
        result=s_nums1.intersection(s_nums2)
        return list(result)
        