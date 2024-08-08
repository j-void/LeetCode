class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        max_points = 1
        for i in range(len(points)):
            hash_map = {}
            for j in range(i+1, len(points)):
                if points[i][0] != points[j][0]:
                    slope = (points[i][1] - points[j][1])/(points[i][0] - points[j][0])
                else:
                    slope = "inf"
                if slope not in hash_map:
                    hash_map[slope] = 2
                else:
                    hash_map[slope] += 1
            if hash_map:
                max_points = max(max_points, max(hash_map.values()))
        
        # print(hash_map)
        return max_points
        
