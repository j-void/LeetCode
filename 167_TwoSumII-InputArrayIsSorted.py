class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            pred = numbers[left] + numbers[right]
            if pred > target:
                right -= 1
            elif pred < target:
                left += 1
            else:
                return [left+1, right+1]
        return [-1, -1]
