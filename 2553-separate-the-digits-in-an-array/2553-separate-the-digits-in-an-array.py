class Solution(object):
    def separateDigits(self, nums):
        result=[]
        for i in nums:
            for j in str(i):
                result.append(int(j))
        return result