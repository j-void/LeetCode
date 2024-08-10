class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        all_chars = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        output = ""
        while columnNumber > 0:
            columnNumber -= 1  
            idx = columnNumber % 26
            output = all_chars[idx] + output
            columnNumber //= 26

        return output        
