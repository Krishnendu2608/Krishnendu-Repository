class Solution(object):
    def missingNumber(self, nums):
        actual_sum=0
        for i in nums:
            actual_sum +=i
        n=len(nums)
        expected_sum= (n*(n+1))/2
        return expected_sum - actual_sum
        

        