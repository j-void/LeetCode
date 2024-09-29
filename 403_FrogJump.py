class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {}
        n = len(stones)
        def helper(i, k):
            if i == n-1:
                return True

            if (i,k) in dp:
                return dp[(i,k)]

            valid = False
            for j in range(i+1, n):
                diff = stones[j]-stones[i]
                if diff == k-1:
                    if helper(j, k-1): return True;
                elif diff == k:
                    if helper(j, k): return True;
                elif diff == k+1:
                    if helper(j, k+1): return True;
            
            dp[(i,k)] = valid
            return valid


        return helper(0, 0)
