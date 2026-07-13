class Solution(object):
    def reverseWords(self, s):
        arr=s.split()
        rev_arr=arr[::-1]
        return " ".join(rev_arr)
       
        