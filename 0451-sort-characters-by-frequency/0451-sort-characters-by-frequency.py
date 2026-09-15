from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        frq=Counter(s)
        highest=frq.most_common()
        arr=[]
        for key,value in highest:
            arr.append(key*value)
        return "".join(arr)
        
        