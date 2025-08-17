class Solution(object):
    def moveZeroes(self, nums):
        l = 0
        while l<len(nums)-1:
            if nums[l]==0 and nums[l+1]!=0:
                nums[l],nums[l+1]=nums[l+1],nums[l]
                if l>0:
                    l-=1
            else:
                l+=1


