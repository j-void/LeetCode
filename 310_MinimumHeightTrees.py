class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1 or not edges:
            return [0]

        in_degree = defaultdict(int)
        graph = defaultdict(list)

        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
            in_degree[e[0]] += 1
            in_degree[e[1]] += 1
        
        queue = deque()
        
        for v,i in in_degree.items():
            if i == 1:
                queue.append(v)

        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(queue)
            remaining_nodes -= leaves_count
            
            for _ in range(leaves_count):
                vertex = queue.popleft()
                for neighbor in graph[vertex]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 1:
                        queue.append(neighbor)
        return list(queue)
