class Solution:
    def originalDigits(self, s: str) -> str:
        char_count = Counter(s)

        count = [0] * 10
        
        count[0] = char_count['z'] 
        count[2] = char_count['w'] 
        count[4] = char_count['u'] 
        count[6] = char_count['x']  
        count[8] = char_count['g']
        
        count[3] = char_count['h'] - count[8]  
        count[5] = char_count['f'] - count[4] 
        count[7] = char_count['s'] - count[6]  
        count[1] = char_count['o'] - count[0] - count[2] - count[4]  
        count[9] = char_count['i'] - count[5] - count[6] - count[8]  
        
        result = ''.join(str(i) * count[i] for i in range(10))
        
        return result
        
