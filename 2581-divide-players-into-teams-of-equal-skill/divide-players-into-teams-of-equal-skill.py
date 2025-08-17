class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill=sorted(skill)
        l=0
        r=len(skill)-1
        x=(skill[l])+(skill[r])
        y=0
        while l<r:
            if (skill[l])+(skill[r])!=x:
                return -1
            y+=(skill[l])*(skill[r])
            l+=1
            r-=1
        return y
        