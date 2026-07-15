class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        frq_s={}
        frq_t={}
        for i in s:
            if i in frq_s:
                frq_s[i] +=1
            elif i not in frq_s:
                frq_s[i]=1
        for j in t:
            if j in frq_t:
                frq_t[j] +=1
            elif j not in frq_t:
                frq_t[j]=1
        if frq_s==frq_t:
            return True
        else:
            return False
        
        