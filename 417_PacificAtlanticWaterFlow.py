class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific = set()
        atlantic = set()
        
        def helper(i, j, region, prev_height):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if heights[i][j] < prev_height:
                return
            if (i, j) in region:
                return
            region.add((i,j)) 
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                helper(ni, nj, region, heights[i][j])  
            return 

        for i in range(m):
            helper(i,0,pacific,-float('inf'))
            helper(i,n-1,atlantic,-float('inf'))
        for i in range(n):
            helper(0,i,pacific,-float('inf'))
            helper(m-1,i,atlantic,-float('inf'))
        
        res = []
        for i in range(m):
            for j in range(n):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])

        return res
