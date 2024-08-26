# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        left, right = 1, n
        while left < right:
            mid = (left+right)//2
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                right = mid-1
            else:
                left = mid+1
        return left
