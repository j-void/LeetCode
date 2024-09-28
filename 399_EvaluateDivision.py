class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i in range(len(equations)):
            v1, v2 = equations[i]
            graph[v1][v2] = values[i]
            graph[v2][v1] = 1.0/values[i]
        
        def helper(s, e):
            queue = deque([(s, 1)])
            visited = set()
            while queue:
                curr_node, curr_value = queue.popleft()
                if curr_node == e:
                    return curr_value
                for k,v in graph[curr_node].items():
                    if k not in visited:
                        visited.add(k)
                        queue.append((k, v*curr_value))
            return -1
        output = []
        for s, e in queries:
            if s not in graph or e not in graph:
                output.append(-1)
                continue
            output.append(helper(s, e))
        return output
        
