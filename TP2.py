from collections import defaultdict, deque
from typing import List, Set, Dict

class GraphAnalyzer:
    def __init__(self, vertex_count: int):
        self.vertex_count = vertex_count
        self._edges: Dict[int, List[int]] = defaultdict(list)
        self._matrix: List[List[int]] = None
    
    def insert_edge(self, origin: int, destination: int) -> None:
        self._edges[origin].append(destination)
        self._matrix = None
        
    def construct_matrix(self) -> List[List[int]]:
        if self._matrix is not None:
            return self._matrix
            
        matrix = [[0] * self.vertex_count for _ in range(self.vertex_count)]
        for source in self._edges:
            for target in self._edges[source]:
                matrix[source - 1][target - 1] = 1
        self._matrix = matrix
        return matrix

    def analyze_weak_components(self) -> int:
        visited: Set[int] = set()
        component_count = 0
        
        undirected: Dict[int, Set[int]] = defaultdict(set)
        for src in self._edges:
            for dst in self._edges[src]:
                undirected[src].add(dst)
                undirected[dst].add(src)
                
        def bfs_traverse(start: int) -> None:
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbor in undirected[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        
        for vertex in range(1, self.vertex_count + 1):
            if vertex not in visited:
                component_count += 1
                visited.add(vertex)
                bfs_traverse(vertex)
                
        return component_count

    def analyze_strong_components(self) -> int:
        visited: Set[int] = set()
        finish_stack: List[int] = []
        
        def dfs_forward(node: int) -> None:
            visited.add(node)
            for next_node in self._edges[node]:
                if next_node not in visited:
                    dfs_forward(next_node)
            finish_stack.append(node)
        
        # Create transposed graph
        transposed = GraphAnalyzer(self.vertex_count)
        for src in self._edges:
            for dst in self._edges[src]:
                transposed.insert_edge(dst, src)
        
        # First DFS pass
        for vertex in range(1, self.vertex_count + 1):
            if vertex not in visited:
                dfs_forward(vertex)
        
        # Second DFS pass on transposed graph
        visited.clear()
        component_count = 0
        
        def dfs_reverse(node: int) -> None:
            visited.add(node)
            for next_node in transposed._edges[node]:
                if next_node not in visited:
                    dfs_reverse(next_node)
        
        # Process in reverse finishing order
        while finish_stack:
            node = finish_stack.pop()
            if node not in visited:
                component_count += 1
                dfs_reverse(node)
                
        return component_count

def main():
    # Test case
    n = 9
    edges = [
    (1, 2), (1, 4), (2, 3), (2, 6), 
    (3, 7), (3, 8), (4, 5), (5, 5), 
    (5, 9), (6, 5), (6, 7), (7, 5), 
    (7, 8), (8, 9),
    ]
    
    analyzer = GraphAnalyzer(n)
    for src, dest in edges:
        analyzer.insert_edge(src, dest)
    
    matrix = analyzer.construct_matrix()
    print("Adjacency Matrix:")
    for row in matrix:
        print(row)
    
    weak = analyzer.analyze_weak_components()
    strong = analyzer.analyze_strong_components()
    
    print("\nNumber of Weakly Connected Components:", weak)
    print("Number of Strongly Connected Components:", strong)

if __name__ == "__main__":
    main()