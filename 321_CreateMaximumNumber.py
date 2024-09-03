class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def get_max(nums, l):
            max_next = len(nums) - l
            stack = []
            for i in range(len(nums)):
                while max_next and stack and stack[-1] < nums[i]:
                    stack.pop()
                    max_next -= 1
                stack.append(nums[i])
             
            return stack[:l]
        
        def merge(l1, l2):
            output = []
            while l1 or l2:
                if l1 > l2:
                    output.append(l1.pop(0))
                else:
                    output.append(l2.pop(0))
            return output
        
        output = [0] * k
        for i in range(k+1):
            j = k-i
            if i > len(nums1) or j > len(nums2):
                continue
            l1 = get_max(nums1, i)
            l2 = get_max(nums2, j)
            new_arr = merge(l1, l2)
            output = max(output, new_arr)
            
        return output
        
