class Solution(object):
    def removeKdigits(self, num, k):
        if len(num)==k:
            return "0"
        stack=[]
        for i in num:
            while stack and stack[-1]>i and k>0:
                stack.pop()
                k-=1
            stack.append(i)
        if k>0:
            stack=stack[:-k]
        result="".join(stack).lstrip("0")
        if result:
            return result
        else:
            return "0"
        