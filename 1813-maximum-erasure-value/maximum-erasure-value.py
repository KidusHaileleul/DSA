class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        x=set()
        i=0
        j=0
        answer=0
        while j < len(nums):
            if nums[j] not in x:
                x.add(nums[j])
                answer=max(answer,sum(nums[i:j+1]))
                j += 1
            else:
                x.remove(nums[i])
                i+=1
        return answer
        