class Solution(object):
    def reverseDegree(self, s):
        total_sum=0
        for i,c in enumerate(s):
            rev_pos=26-(ord(c)-ord("a"))
            total_sum+=rev_pos*(i+1)
        return total_sum
        