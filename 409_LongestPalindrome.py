class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        output = 0
        for k,v in count.items():
            if v % 2 == 0:
                output += v
                count[k] -= v
            else:
                output += (v-1)
                count[k] -= (v-1)
        for k,v in count.items():
            if v > 0:
                output += 1
                break
        return output
