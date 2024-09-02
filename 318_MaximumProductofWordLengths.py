class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        
        bitmasks = [0] * len(words)
        for i in range(len(words)):
            b = 0
            for c in words[i]:
                b = b | (1 << ord(c) - ord('a'))
            bitmasks[i] = b


        output = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if bitmasks[i] & bitmasks[j] == 0:
                    output = max(output, len(words[i])*len(words[j]))
        return output
