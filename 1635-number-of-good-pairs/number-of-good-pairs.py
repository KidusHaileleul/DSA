class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        x = len(nums)
        for i in range(x):
            for j in range(i + 1, x):
                if nums[i] == nums[j]:
                    count += 1
        return count

        