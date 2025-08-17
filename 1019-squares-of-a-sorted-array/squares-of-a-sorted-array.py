class Solution:
    def sortedSquares(self, num: List[int]) -> List[int]:
        L=0
        R=len(num)-1
        result=[]
        while L<=R:
            if abs(num[L])>abs(num[R]):
                result.append(num[L]**2)
                L+=1
            else:
                result.append(num[R]**2)
                R-=1
        result.reverse()
        return result
        