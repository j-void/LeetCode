class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = defaultdict(int)
        for c in s:
            s_dict[c] += 1
        for c in t:
            s_dict[c] -= 1
            if s_dict[c] < 0:
                return c
        return ""
