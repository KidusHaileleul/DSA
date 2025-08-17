class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        x=[]
        for i in range(len(nums)):
            y=nums[i]**2
            x.append(y)
        return sorted(x)
        