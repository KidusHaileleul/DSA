class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        x=len(p)
        n=len(s)
        l=0
        y=[]
        p_counter=Counter(p)

        while x<=n:
            anagram=s[l:x]
            anagram_counter=Counter(anagram)
            if p_counter==anagram_counter:
                y.append(l)
                l+=1
                x+=1
            else:
                l+=1
                x+=1
        return y


        