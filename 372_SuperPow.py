class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        
        def pow(a, b):
            output = 1
            a = a%1337
            for _ in range(b):
                output = (output*a) % 1337
            
            return output
            
        res = 1
        for i in range(len(b)-1, -1, -1):
            res = (res * pow(a, b[i])) % 1337
            a = pow(a, 10)  

        return res
