class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for col in zip(*strs):
            col=list(col)
            if col!=sorted(col):
                count+=1
        return count
        