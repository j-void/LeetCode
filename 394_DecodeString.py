
class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        queue = []

        cnum = "0"
        for i in range(len(s)):
            print(stack, queue)
            if s[i].isdigit():
                cnum += s[i]
            else:
                if cnum != "0":
                    queue.append(int(cnum))
                cnum = "0"
                if s[i] == "[":
                    stack.append("")
                elif s[i] == "]":
                    cs = stack.pop()
                    count = queue.pop() if queue else 1
                    if stack:
                        stack[-1] += (cs*count)
                    else:
                        stack.append(cs*count)
                else:
                    if stack:
                        stack[-1] += s[i]
                    else:
                        stack.append(s[i])
        return stack[0]
