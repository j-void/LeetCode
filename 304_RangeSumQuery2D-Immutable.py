class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix_sum = [[0 for _ in range(cols)] for _ in range(rows)]
        self.prefix_sum[0][0] = matrix[0][0]
        for i in range(1, rows):
            self.prefix_sum[i][0] = self.prefix_sum[i-1][0] + matrix[i][0]
        for i in range(1, cols):
            self.prefix_sum[0][i] = self.prefix_sum[0][i-1] + matrix[0][i]
        for i in range(1, rows):
            for j in range(1, cols):
                self.prefix_sum[i][j] = self.prefix_sum[i-1][j] - self.prefix_sum[i-1][j-1] + self.prefix_sum[i][j-1] + self.matrix[i][j]
        
        print(self.prefix_sum)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.prefix_sum[row2][col2]
        b = 0 if col1 == 0 else self.prefix_sum[row2][col1-1]
        c = 0 if row1 == 0 else self.prefix_sum[row1-1][col2]
        d = 0 if row1 == 0 or col1 == 0 else self.prefix_sum[row1-1][col1-1]

        return a - b - (c-d)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
