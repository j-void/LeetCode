class Solution:
    def lengthLongestPath(self, input: str) -> int:
        levels = defaultdict(list)
        input_ = input.split("\n")
        output = 0
        for p in input_:
            c = p.count("\t")
            if levels[c-1]:
                levels[c].append(levels[c-1][-1]+len(p)-c)
            else:
                levels[c].append(len(p)-c)
            if "." in p:
                output = max(output, levels[c][-1]+c)

        return output
        
