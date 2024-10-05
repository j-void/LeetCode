class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        d = len(num1) - len(num2)
        num2 = "0"*d+num2
        carry = 0
        output = ""
        for i in range(len(num1)-1, -1, -1):
            s = int(num1[i])+int(num2[i]) + carry
            carry = s//10
            r = s%10
            output = str(r) + output
        if carry != 0:
            output = str(carry) + output
        return output

#digit1 = ord(num1[d1]) - ord('0') if d1 >= 0 else 0
#digit2 = ord(num2[d2]) - ord('0') if d2 >= 0 else 0
