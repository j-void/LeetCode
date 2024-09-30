class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        output = ""
        conversion = {i:str(i) for i in range(10)}
        conversion[10] = "a"
        conversion[11] = "b"
        conversion[12] = "c"
        conversion[13] = "d"
        conversion[14] = "e"
        conversion[15] = "f"

        if num < 0:
            num += 2**32

        while num:
            rmdr = num % 16
            num = num // 16
            output = conversion[rmdr] + output
        
        return output
