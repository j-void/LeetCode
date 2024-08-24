class Solution:
    def calculate(self, s: str) -> int:
        pre_op = "+"
        stack = []
        num = 0
        for c in s+"+":
            if c.isdigit():
                num = num*10 + int(c)
            elif c in "+-*/":
                if pre_op == "+":
                    stack.append(num)
                elif pre_op == "-":
                    stack.append(-num)
                elif pre_op == "*":
                    stack.append(stack.pop()*num)
                elif pre_op == "/":
                    stack.append(int(stack.pop()/num))
                pre_op = c
                num = 0
        return sum(stack)
