class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.idx = -1


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_dict = {words[i]:i for i in range(len(words))}
        output = []
        for i in range(len(words)):
            word = words[i]
            for j in range(len(word)+1):
                prefix = word[:j]
                suffix = word[j:]

                if prefix == prefix[::-1]:
                    reversed_suffix = suffix[::-1]
                    if reversed_suffix in word_dict and word_dict[reversed_suffix] != i:
                        output.append([word_dict[reversed_suffix],i])
                
                if j!= len(word) and suffix == suffix[::-1]:
                    reversed_prefix = prefix[::-1]
                    if reversed_prefix in word_dict and word_dict[reversed_prefix] != i:
                        output.append([i, word_dict[reversed_prefix]])
        
        return output

