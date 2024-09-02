class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_seen = {s[i]:i for i in range(len(s))}
        visited = set()
        stack = []

        for i,c in enumerate(s):
            if c not in visited:
                while stack and stack[-1] > c and last_seen[stack[-1]] > i:
                    visited.remove(stack.pop())
                    
                stack.append(c)
                visited.add(c)
        print(stack)
        return "".join(stack)
