class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        paired = list(zip(heights, names))
        new_paired=list(reversed(sorted(paired)))
        return [name for height, name in new_paired]
        