class Solution(object):
    def isPowerOfFour(self, n):
        if n<0:
            return False
        elif(n & (n-1)==0) and ((n-1)%3==0):
            return True
        else: 
            return False
        