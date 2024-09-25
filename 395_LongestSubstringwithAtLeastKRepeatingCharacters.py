class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        def helper(s):
            if not s:
                return 0
            count = defaultdict(int)
            for c in s:
                count[c] += 1
            for i in range(len(s)):
                if count[s[i]] < k:
                    left = helper(s[:i])
                    right = helper(s[i+1:])
                    return max(left, right)
            return len(s)
        
        return helper(s)
