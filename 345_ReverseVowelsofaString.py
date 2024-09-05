class Solution:
    def reverseVowels(self, s: str) -> str:
        vovels = set(["a", "e", "i", "o", "u"])
        s = list(s)
        i,j = 0, len(s)-1
        while i < j:
            iv = s[i].lower() in vovels
            jv = s[j].lower() in vovels
            if iv and jv:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif iv and not jv:
                j -= 1
            elif jv and not iv:
                i += 1
            else:
                i += 1
                j -= 1
        return "".join(s)
