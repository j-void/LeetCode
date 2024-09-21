class Solution:

    def __init__(self, nums: List[int]):
        self.init_array = nums[:]
        self.array = nums

    def reset(self) -> List[int]:
        for i in range(len(self.array)):
            self.array[i] = self.init_array[i]
        return self.array
        

    def shuffle(self) -> List[int]:
        random.shuffle(self.array)
        return self.array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
