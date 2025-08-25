class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        y = []
        s = sum(nums[i:k])
        y.append(s)
        while k < len(nums):
            s += nums[k] - nums[i]
            y.append(s)
            i += 1
            k += 1

        return max(y) / (k - i)


            

        