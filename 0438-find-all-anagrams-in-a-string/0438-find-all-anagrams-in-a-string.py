from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        k=len(p)
        window_counter=Counter(s[0:k])
        anagram_counter=Counter(p)
        arr=[]
        if window_counter==anagram_counter:
            arr.append(0)
        for i in range(len(s)-k):
            trailing_char=s[i]
            leading_char=s[i+k]
            window_counter[trailing_char]-=1
            if window_counter[trailing_char]==0:
                del window_counter[trailing_char]
            window_counter[leading_char]+=1
            if window_counter==anagram_counter:
                arr.append(i+1)
        return arr
        
        