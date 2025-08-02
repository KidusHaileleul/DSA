class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        y = []
        n = len(nums)
        count = Counter(nums)
        for x in count:
            if count[x] > n // 3:
                y.append(x)
        return y
        