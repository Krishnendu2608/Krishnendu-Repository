class Solution(object):
    def searchInsert(self, nums, target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid_index=(left+right)//2
            mid_number=nums[mid_index]
            if target==mid_number:
                return mid_index
            elif target<mid_number:
                right=mid_index-1
            elif target>mid_number:
                left=mid_index+1
        return left
        
        