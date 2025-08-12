class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        paired = list(zip(heights, names))
        for i in range(len(paired)):
            for j in range(i+1, len(paired)):
                if paired[i] < paired[j]:  
                    paired[i], paired[j] = paired[j], paired[i]
        return [name for _, name in paired]
        