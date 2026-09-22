class Solution(object):
    def minimumRounds(self, tasks):
        total=0
        frq={}
        for i in tasks:
            if i in frq:
                frq[i]+=1
            else:
                frq[i]=1
        for key,values in frq.items():
            if values==1:
                return -1
            else:
                rounds=(values+2)//3
                total+=rounds
        return total
        