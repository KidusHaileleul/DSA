class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        n=len(nums)
        count=0
        l=0
        r=n-1
        while l<r:
            if nums[l]+nums[r]<target:
                count+=(r-l)
                l+=1
            else:
                r-=1
        return count


                    