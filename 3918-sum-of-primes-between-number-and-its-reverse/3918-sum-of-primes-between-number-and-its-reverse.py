class Solution(object):
    def is_prime(self,num):
        if num<=1:
            return False
        for i in range(2,num):
            if num%i==0:
                return False
        return True
    def sumOfPrimesInRange(self, n):
        rev_n=0
        temp=n
        while temp>0:
            rem=temp%10
            rev_n=(rev_n*10)+rem
            temp=temp//10
        total=0
        for i in range(min(n,rev_n),max(n,rev_n)+1):
            if self.is_prime(i)==True:
                total+=i
        return total
            
            
        