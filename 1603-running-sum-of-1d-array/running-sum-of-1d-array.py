class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        nums_copy=nums.copy()
        for i in range(len(nums)):
            nums[i]=sum(nums_copy[:i+1])
        return nums
            
        