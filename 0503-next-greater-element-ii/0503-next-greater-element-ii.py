class Solution(object):
    def nextGreaterElements(self, nums):
        n=len(nums)
        ans=[-1]*n
        stack=[]
        for i in range(2*n):
            curr_num=nums[i%n]
            while stack and curr_num>nums[stack[-1]]:
                popped_index=stack.pop()
                ans[popped_index]=curr_num
            if i<n:
                stack.append(i)
        return ans        