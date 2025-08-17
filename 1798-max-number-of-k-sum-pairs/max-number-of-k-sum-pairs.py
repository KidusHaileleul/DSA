class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        n=len(nums)
        l=0
        r=n-1
        count=0
        while l<r:
            if nums[l]+nums[r]<k:
                l+=1
            elif nums[l]+nums[r]==k:
                count+=1
                l += 1
                r -= 1
            else:
                r-=1
        return count
        