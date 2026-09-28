class Solution(object):
    def letterCasePermutation(self, s):
        res=[]
        def backtrack(idx,curr_string):
            if idx==len(s):
                res.append(curr_string)
                return

            if s[idx].isalpha():
                backtrack(idx+1,curr_string+s[idx].lower())
                backtrack(idx+1,curr_string+s[idx].upper())
            else:
                backtrack(idx+1,curr_string+s[idx])     
        backtrack(0,"")
        return res  