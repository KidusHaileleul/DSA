class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        x=set()
        l=0
        res=float('inf')
        for r in range(len(cards)):
            while cards[r] in x:
                res=min(res,r-l+1)
                x.remove(cards[l])
                l+=1
            x.add(cards[r])
        return res if res!=float('inf') else -1

        