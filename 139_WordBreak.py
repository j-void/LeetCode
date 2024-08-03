class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict:
            return False
        # def helper(s):
        #     if not s:
        #         return True
        #     for i in range(len(s)):
        #         if s[:i+1] in wordDict:
        #             if i == len(s)-1:
        #                 return True 
        #             if helper(s[i+1:]):
        #                 return True

        #     return False

        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for w in wordDict:
                start = i-len(w)
                if start < 0:
                    continue
                if w == s[start:i] and dp[start]:
                    dp[i] = True
                    break
        
        return dp[-1]
