class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dict = {}
        s_dict = {}
        s = s.split()
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            p_present = pattern[i] in pattern_dict
            s_present = s[i] in s_dict
            if not p_present and not s_present:
                pattern_dict[pattern[i]] = s[i]
                s_dict[s[i]] = pattern[i]
            elif (s_present and not p_present) or (not s_present and p_present):
                return False
            elif pattern_dict[pattern[i]] != s[i] or s_dict[s[i]] != pattern[i]:
                return False

        return True
