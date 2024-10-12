class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        fresh_oranges = 0
        queue = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    queue.append((i,j,0))
        if fresh_oranges == 0:
            return 0

        while queue:
            i,j,t = queue.popleft()
            for di,dj in [(-1,0), (1,0), (0, -1), (0,1)]:
                ci, cj = i+di, j+dj
                if ci < 0 or ci > n-1 or cj < 0 or cj > m-1:
                    continue
                if (ci,cj) not in visited and grid[ci][cj]==1:
                    fresh_oranges -= 1
                    visited.add((ci,cj))
                    queue.append((ci,cj,t+1))
                if fresh_oranges == 0:
                    return t+1
        return -1

            
