class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_dict = defaultdict(int)
        guess_dict = defaultdict(int)
        x,y = 0,0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                x += 1
            else:
                secret_dict[secret[i]] += 1
                guess_dict[guess[i]] += 1
        
        for k,v in guess_dict.items():
            if k in secret_dict:
                y += min(v, secret_dict[k])
        
        return str(x)+"A"+str(y)+"B"
