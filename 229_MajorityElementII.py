class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2 = None, None
        count1, count2 = 0, 0
        for n in nums:
            if n == num1:
                count1 += 1 
            elif n == num2:
                count2 += 1
            elif count1 == 0:
                num1, count1 = n, 1
            elif count2 == 0:
                num2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        
        output = []
        if num1 is not None and nums.count(num1) > len(nums)//3:
            output.append(num1)
        if num2 is not None and nums.count(num2) > len(nums)//3:
            output.append(num2)
        return output
