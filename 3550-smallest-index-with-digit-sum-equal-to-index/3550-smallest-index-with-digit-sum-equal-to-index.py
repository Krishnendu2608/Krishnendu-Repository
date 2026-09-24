class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            temp=nums[i]
            total=0
            while temp>0:
                last_dig=temp%10
                total+=last_dig
                temp=temp//10
            if total==i:
                return i
                break
        return -1


        