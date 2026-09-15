class Solution(object):
    def countDistinctIntegers(self, nums):
        seen=set()
        for i in nums:
            seen.add(i)
            rev=int(str(i)[::-1])
            seen.add(rev)
        return len(seen)
        