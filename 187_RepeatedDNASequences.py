class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hash_map = defaultdict(int)
        for i in range(len(s)-9):
            hash_map[s[i:i+10]] += 1
        output = []
        for k,v in hash_map.items():
            if v > 1:
                output.append(k)
        return output
