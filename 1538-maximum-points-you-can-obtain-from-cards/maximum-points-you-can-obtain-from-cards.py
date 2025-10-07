class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l=0
        x=len(cardPoints)-k
        summ=sum(cardPoints[:x])
        minn=summ
        while x<len(cardPoints):
            summ+=cardPoints[x]-cardPoints[l]
            minn=min(minn,summ)
            l+=1
            x+=1
        return sum(cardPoints)-minn



        