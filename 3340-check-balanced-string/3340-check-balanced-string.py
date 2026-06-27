class Solution(object):
    def isBalanced(self, num):
        even=0
        odd=0
        
        for i,j in enumerate(num):
            if i%2==0:
                even=even+int(j)
            else:
                odd=odd+int(j)
        if even==odd:
            return True
        else:
            return False
