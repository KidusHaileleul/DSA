class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        columns = len(matrix[0])
        result = []
        for i in range(columns):
            new_row = []
            for j in range(rows):
                new_row.append(matrix[j][i])
            result.append(new_row)
        return result

        