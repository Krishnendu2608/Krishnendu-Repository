class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        start=x
        digit=0
        while x>0:
            number=x%10
            digit=number+digit*10
            x=x//10
        if start==digit:
            return True
        else:
            return False

    

        