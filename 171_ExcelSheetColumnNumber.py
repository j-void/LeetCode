class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        all_chars = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        hash_map = {all_chars[i]:i+1 for i in range(len(all_chars))}

        output = 0
        for i in range(len(columnTitle)):
            output = (26 * output) + hash_map[columnTitle[i]] 
        
        return output
