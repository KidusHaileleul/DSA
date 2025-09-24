class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white=0
        for i in range(k):
            if blocks[i]=="W":
                white+=1
        min_len=white
        for r in range(k,len(blocks)):
            if blocks[r]=="W":
                white+=1
            if blocks[r-k]=="W":
                white-=1
            min_len=min(min_len,white)
        return min_len



        
        