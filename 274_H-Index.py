class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        hidx = 0
        for i in range(n):
            hidx = max(hidx, min(citations[i], n-i))
        return hidx
