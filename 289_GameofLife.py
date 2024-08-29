class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])
        
        def get_value(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return 0
            return board[i][j]

        region = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]
        for i in range(rows):
            for j in range(cols):
                val = 0
                for dx,dy in region:
                    val += get_value(i+dx, j+dy) in [1, -1]
                if (board[i][j] == 0 or board[i][j] == 2) and val == 3:
                    board[i][j] = 2
                elif board[i][j] == 1 or board[i][j] == -1:
                    if val < 2 or val > 3:
                        board[i][j] = -1
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1

        
