class Solution(object):
    def maxVowels(self, s, k):
        vowels=["a","e","i","o","u"]
        current_vowel=0
        for i in range(k):
            if s[i] in vowels:
                current_vowel +=1
        max_vowel=current_vowel
        for i in range(0,len(s)-k):
            trailing_char=s[i]
            leading_char=s[i+k]
            if trailing_char in vowels:
                current_vowel-=1
            if leading_char in vowels:
                current_vowel+=1
            max_vowel=max(current_vowel,max_vowel)
        return max_vowel
