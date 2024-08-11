# class LargerKey(str):
#     def __lt__(x,y):
#         return x+y > y+x
# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         nums_str = [str(n) for n in nums]

#         nums_str.sort(key=LargerKey)
#         if nums_str[0] == "0":
#             return "0"
#         return "".join(nums_str).lstrip('0')
    
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = [str(n) for n in nums]
        def compare(x,y):
            if x+y > y+x:
                return -1
            else:
                return 1
        nums_str.sort(key=cmp_to_key(compare))
        if nums_str[0] == "0":
            return "0"
        return "".join(nums_str).lstrip('0')
