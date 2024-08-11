class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sum(num):
            output = 0
            while num > 0:
                digit = num % 10
                num = num // 10
                output += (digit**2)
            return output

        visited = set()
        while n not in visited:
            visited.add(n)
            n = get_sum(n)
            if n == 1:
                return True

        return False
        
