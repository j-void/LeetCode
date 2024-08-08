class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        stack = []
        for t in tokens:
            if t == "+":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num1+num2)
            elif t == "-":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num2-num1)
            elif t == "*":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num1*num2)
            elif t == "/":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num2/num1)
            else:
                stack.append(int(t))

        return int(stack[-1])
        
