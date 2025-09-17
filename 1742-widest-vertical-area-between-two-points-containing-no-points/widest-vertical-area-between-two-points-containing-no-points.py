class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x=[]
        for i in points:
            x.append(i[0])
        x.sort()
        maxx=0
        for j in range(1,len(x)):
            maxx=max(maxx,x[j]-x[j-1])
        return maxx
