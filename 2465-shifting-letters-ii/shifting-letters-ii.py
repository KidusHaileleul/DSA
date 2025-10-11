class Solution:
    def shiftingLetters(self,s: str,shifts: List[List[int]]) -> str:
        def shift_forward(c,v):
            return chr((ord(c)-97+v)%26+97)
        n=len(s)
        x=[0]*(n+1)
        for start,end,direction in shifts:
            if direction==1:
                x[start]+=1
                x[end+1]-=1
            else:
                x[start]-=1
                x[end+1]+=1
        for i in range(1,n):
            x[i]+=x[i-1]
        new_s=""
        for i in range(n):
            new_s+=shift_forward(s[i],x[i])
        return new_s
 