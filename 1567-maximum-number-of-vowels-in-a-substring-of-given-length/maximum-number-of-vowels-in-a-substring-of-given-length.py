class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v=set("aeiou")
        l=0
        count=0
        maxx=0
        for r in range(len(s)):
            if s[r] in v:
                count+=1
            while r - l + 1 > k:
                if s[l] in v:
                    count-=1
                l+=1
            maxx=max(maxx,count)
        return maxx


        