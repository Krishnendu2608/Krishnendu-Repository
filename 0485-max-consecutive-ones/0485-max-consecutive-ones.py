class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=0
        arr=[]
        for i in nums:
            if i==1:
                count +=1
            elif i !=1:
                arr.append(count)
                count=0
            arr.append(count)
        return max(arr)
        