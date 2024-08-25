class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor = xor ^ num
        
        bit = xor & -xor
        num1, num2 = 0, 0
        for num in nums:
            if num & bit:
                num1 = num1 ^ num
            else:
                num2 = num2 ^ num

        return [num1, num2]
        
