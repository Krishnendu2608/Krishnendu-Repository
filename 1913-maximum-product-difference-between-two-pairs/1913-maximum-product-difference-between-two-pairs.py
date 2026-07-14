class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()
        max_diff=(nums[-1]*nums[-2])-(nums[0]*nums[1])
        return max_diff
