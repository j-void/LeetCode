class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = {}
        def helper(i,j): ## mincost between i->j
            if i >= j:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            out = float('inf')
            for h in range(i, j+1):
                ## see graph, curr val + left tree + right tree
                curr_cost = h + max(helper(i,h-1), helper(h+1,j))
                out = min(out, curr_cost)
            dp[(i,j)] = out
            return out

        return helper(1,n) 
