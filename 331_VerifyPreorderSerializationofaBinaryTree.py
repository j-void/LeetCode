class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        inDegree = 1
        nodes = preorder.split(',')
        for node in nodes:
            inDegree -= 1

            if inDegree < 0:
                return False

            if node != "#":
                inDegree += 2

        return inDegree==0
         
