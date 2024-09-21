class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rmap = defaultdict(int)
        for c in magazine:
            rmap[c] += 1
        for c in ransomNote:
            if c not in rmap:
                return False
            rmap[c] -= 1
            if rmap[c] == 0:
                del rmap[c]

        return True
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in set(ransomNote):
            if ransomNote.count(letter) > magazine.count(letter):
                return False

        return True
