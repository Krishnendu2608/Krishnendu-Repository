class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        most=max(candies)
        result=[]
        for i in candies:
            if i+extraCandies >= most:
                result.append(True)
            elif i+extraCandies<most:
                result.append(False)
        return result
                 
        