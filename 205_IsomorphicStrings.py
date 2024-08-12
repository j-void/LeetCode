class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map_s = {}
        hash_map_t = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in hash_map_s and hash_map_s[s[i]] != t[i]:
                return False
            elif t[i] in hash_map_t and hash_map_t[t[i]] != s[i]:
                return False
            hash_map_s[s[i]] = t[i]
            hash_map_t[t[i]] = s[i]
        
        return True
