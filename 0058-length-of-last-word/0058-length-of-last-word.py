class Solution(object):
    def lengthOfLastWord(self, s):
        arr=s.split()
        last=arr[-1]
        return len(last)