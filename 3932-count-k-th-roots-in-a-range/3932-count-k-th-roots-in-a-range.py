class Solution(object):
    def countKthRoots(self, l, r, k):
        if k==1:
            return r-l+1
        count=0
        x=0
        while True:
            y=x**k
            if y>r:
                break
            elif l<=y<=r:
                count+=1
            x+=1
        return count
        