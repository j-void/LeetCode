class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.idx = defaultdict(set)

    def insert(self, val: int) -> bool:
        # print("is", self.idx)
        output = True
        if val in self.idx:
            output = False
        self.idx[val].add(len(self.nums))
        self.nums.append(val)
        # print("ie", self.idx)
        return output

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False

        remove_idx = self.idx[val].pop()  
        
        last_val = self.nums[-1]
        
        if remove_idx != len(self.nums) - 1:
            self.nums[remove_idx] = last_val
            self.idx[last_val].add(remove_idx)
            self.idx[last_val].remove(len(self.nums) - 1)
        
        self.nums.pop()

        if not self.idx[val]:
            del self.idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
