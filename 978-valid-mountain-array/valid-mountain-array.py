class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        n = max(arr)
        x = arr.index(n)
        if x == 0 or x == len(arr) - 1:
            return False
        if arr.count(n) != 1:
            return False
        y = arr[:x]
        z = arr[x+1:]
        q = sorted(y)
        r = sorted(z)
        if len(y) != len(set(y)):
            return False
        elif len(z) != len(set(z)):
            return False
        elif y == q and z == r[::-1]:
            return True
        else:
            return False

        