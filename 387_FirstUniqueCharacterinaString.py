class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_dict = defaultdict(int)
        for c in s:
            count_dict[c] += 1
        
        for i in range(len(s)):
            if count_dict[s[i]] == 1:
                return i
        return -1
