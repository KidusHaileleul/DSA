class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v=set("aeiou")
        l=0
        count=0
        for i in range(k):
            if s[i] in v:
                count+=1
        max_vowel=count
        for r in range(k,len(s)):
            if s[r] in v:
                count+=1
            if s[l] in v:
                count-=1
            l+=1
            max_vowel=max(max_vowel,count)
        return max_vowel



        