class NumArray(object):
    def __init__(self, nums):
        self.prefix=[0]
        x=0
        for i in nums:
            x+=i
            self.prefix.append(x)
    def sumRange(self, left, right):
        return self.prefix[right+1]-self.prefix[left]
