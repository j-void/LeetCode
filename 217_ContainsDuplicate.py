class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = defaultdict(int)
        for n in nums:
            hash_map[n] += 1
            if hash_map[n] >= 2:
                return True
        return False
