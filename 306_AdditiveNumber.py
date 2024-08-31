class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        def helper(num, path):
            if not num:
                if len(path) > 2:
                    return True
                return False
            out = False
            for i in range(len(num)):
                cw = num[:i+1]
                if len(cw) > 1 and cw[0] == '0':
                    break
                if len(path) < 2 or path[-1]+path[-2] == int(cw):
                    out = out or helper(num[i+1:], path+[int(cw)])
            return out

        

        return helper(num, [])
