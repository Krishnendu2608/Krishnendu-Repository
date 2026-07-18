class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        frq1={}
        frq2={}
        for i in ransomNote:
            if i in frq1:
                frq1[i]+=1
            elif i not in frq1: 
                frq1[i]=1
        for j in magazine:
            if j in frq2:
                frq2[j]+=1
            elif j not in frq2: 
                frq2[j]=1        
        for k in frq1:
            if k not in frq2 or frq1[k]>frq2[k]:
                return False
        return True