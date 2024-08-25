class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        dp = {}
        def helper(exp):
            if exp in dp:
                return dp[exp]
            if exp.isdigit():
                dp[exp] = [int(exp)]
                return [int(exp)]
            res = []
            for i in range(len(exp)):
                if exp[i] in "-+*":
                    left = helper(exp[:i])
                    right = helper(exp[i+1:])
                    for l in left:
                        for r in right:
                            if exp[i] == "+":
                                res.append(l+r)
                            elif exp[i] == "-":
                                res.append(l-r)
                            elif exp[i] == "*":
                                res.append(l*r)
            dp[exp] = res      
            return res
        output = helper(expression)

        return output
        
