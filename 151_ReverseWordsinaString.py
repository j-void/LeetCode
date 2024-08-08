class Solution:
    # def reverseWords(self, s: str) -> str:
    #     words = s.split()
    #     words = words[::-1]
    #     return " ".join(words)
    def reverseWords(self, s: str) -> str:
        if not s:return;
        curr_word = ""
        sentence = ""
        for c in s:
            if c.isspace():
                if curr_word:
                    if sentence:
                        sentence = curr_word +" "+ sentence
                    else:
                        sentence = curr_word
                    curr_word = ""
            else:
                curr_word += c
        if curr_word:
            if sentence:
                sentence = curr_word +" "+ sentence
            else:
                sentence = curr_word
        return sentence
