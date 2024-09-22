class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        output = []
        def helper(i):
            if i > n:
                return
            for j in range(10):
                num = i*10+j
                if num == 0:
                    continue
                if num <= n:
                    output.append(num)
                    helper(num)
                else:
                    break
            return
        
        helper(0)

        return output
