class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        visited = set()
        m = len(board)
        n = len(board[0])

        def helper(r,c):
            if (r,c) in visited:
                return
            for i in range(r+1, m):
                if board[i][c] != 'X' or (i,c) in visited:
                    break
                visited.add((i,c))
            for i in range(c+1, n):
                if board[r][i] != 'X' or (r,i) in visited:
                    break
                visited.add((r,i))
            return
        output = 0
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'X' and (r,c) not in visited:
                    helper(r,c)
                    output += 1
        return output
