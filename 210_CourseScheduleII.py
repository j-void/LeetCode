class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]
        graph = defaultdict(list)
        in_edges = defaultdict(int)

        for u,v in prerequisites:
            graph[v].append(u)
            in_edges[u] += 1
        
        queue = collections.deque()
        for i in range(numCourses):
            if in_edges[i] == 0:
                queue.append(i)

        path = []
        while queue:
            node = queue.popleft()
            path.append(node)
            for idx, neighbour in enumerate(graph[node]):
                in_edges[neighbour] -= 1
                if in_edges[neighbour] == 0:
                    queue.append(neighbour)
        return path if len(path) == numCourses else []

        
