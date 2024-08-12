class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for u,v in prerequisites:
            graph[u].append(v)
            in_degree[v] += 1
        
        queue = [node for node in graph if in_degree[node] == 0]
        count = 0
        while queue:
            node = queue.pop(0)
            count += 1 
            
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return count == len(in_degree)
        
