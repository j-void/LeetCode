class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        front = ""
        back = ""
        rem_hash = {}
        i = 0
        neg = 1
        if numerator < 0:
            neg *= -1
            numerator = abs(numerator)
        if denominator < 0:
            neg *= -1
            denominator = abs(denominator)
        while numerator > 0:
            if numerator >= denominator:
                div = numerator // denominator
                numerator = numerator % denominator
                front += str(div)
            else:
                if numerator in rem_hash:
                    idx = rem_hash[numerator]
                    rep = "("+back[idx:]+")"
                    back = back[:idx] + rep
                    break
                div = (numerator*10) // denominator
                back += str(div)
                rem_hash[numerator] = int(len(back))-1
                numerator = (numerator*10) % denominator
            i += 1
            # print(rem_hash, numerator)
        # print(front, back, rem_hash)
        if not front:
            front = "0"
        if neg == -1:
            front = "-"+front
        if back:
            return front+"."+back
        else:
            return front
        
        return ""
        
