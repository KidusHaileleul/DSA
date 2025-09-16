class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        zero=0
        max_len=0
        for r in range(len(nums)):
            if nums[r]==0:
                zero+=1
            while zero>1:
                if nums[l]==0:
                    zero-=1
                l+=1
            max_len=max(max_len,r-l)
        return max_len




        