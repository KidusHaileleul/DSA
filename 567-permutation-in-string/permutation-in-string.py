class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count=Counter(s1)
        n=len(s1)
        l=0
        while n<=len(s2):
            if Counter(s2[l:n])==s1_count:
                return True
            l+=1
            n+=1
        return False



            
        