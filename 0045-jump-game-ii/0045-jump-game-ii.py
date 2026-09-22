class Solution(object):
    def jump(self, nums):
        if len(nums)<=1:
            return 0
        curr_end=0
        far=0
        jump=0
        for i in range(len(nums)-1):
            far=max(far,i+nums[i])
            if i==curr_end:
                jump+=1
                curr_end=far
                if curr_end>=len(nums)-1:
                    break
        return jump
        