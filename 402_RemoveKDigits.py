class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for n in list(map(int, num)):
            while stack and k > 0 and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        if k > 0: 
            stack = stack[:-k]
        
        output = "".join(list(map(str, stack))).lstrip("0")

        return output if output else "0"
