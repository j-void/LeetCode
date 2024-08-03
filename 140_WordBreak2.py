class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s or not wordDict:
            return []
        wordDict = set(wordDict)
        output = []
        def helper(s, out):
            if not s:
                output.append(out)
            for i in range(len(s)):
                if s[:i+1] in wordDict:
                    out_new = out+" "+s[:i+1] if out else s[:i+1]
                    helper(s[i+1:], out_new)
        helper(s, "")
        return output
