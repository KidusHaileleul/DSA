class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ=0
        min_len=float("inf")
        l=0
        for r in range(len(nums)):
            summ+=nums[r]
            while summ>=target:
                min_len=min(min_len,r-l+1)
                summ-=nums[l]
                l+=1
        if min_len<float("inf"):
            return min_len
        else:
            return 0
        

        
        
        