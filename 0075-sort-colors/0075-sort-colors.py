class Solution(object):
    def sortColors(self, nums):
        count0=0
        count1=0
        count2=0
        index=0
        for i in nums:
            if i==0:
                count0 +=1
            elif i==1:
                count1 +=1
            elif i==2:
                count2 +=1
        for j in range(count0):
            nums[index]=0
            index +=1
        for k in range(count1):
            nums[index]=1
            index +=1
        for l in range(count2):
            nums[index]=2
            index +=1
        return nums


        