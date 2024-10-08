class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        start = 0
        max_len = 0
        max_freq = 0
        curr = defaultdict(int)
        for i in range(len(s)):
            curr[s[i]] += 1
            max_freq = max(max_freq, curr[s[i]])

            if i-start+1-max_freq > k:
                curr[s[start]] -= 1
                start += 1
            
            max_len = max(max_len, i-start+1)
        return max_len

        
