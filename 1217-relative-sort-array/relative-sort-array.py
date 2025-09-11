class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        x = []
        y = Counter(arr1)
        for i in arr2:
            x.extend([i] * y[i])
        for num in sorted(y.elements()):
            if num not in arr2:
                x.append(num)
        return x
        