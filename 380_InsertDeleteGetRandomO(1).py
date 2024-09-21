class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.idx = {}

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        self.idx[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        lnum = self.nums[-1]
        self.nums[self.idx[val]], self.nums[-1] = self.nums[-1], self.nums[self.idx[val]]
        self.idx[lnum] = self.idx[val]
        self.nums.pop()
        del self.idx[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
