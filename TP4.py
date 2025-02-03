import heapq

def prim_mst_dict(graph, root):
    mst_edges = []
    total_weight = 0
    visited = {node: False for node in graph}
    priority_queue = [(0, root, None)]  # (weight, current_node, parent_node)

    while priority_queue:
        weight, current_node, parent_node = heapq.heappop(priority_queue)

        if visited[current_node]:
            continue
        visited[current_node] = True

        if parent_node is not None:
            mst_edges.append((parent_node, current_node, weight))
            total_weight += weight

        for neighbor, edge_weight in graph[current_node].items():
            if not visited[neighbor]:
                heapq.heappush(priority_queue, (edge_weight, neighbor, current_node))

    return mst_edges, total_weight

def kruskal_mst_dict(graph):
    edges = []
    for u in graph:
        for v, weight in graph[u].items():
            if u < v:
                edges.append((u, v, weight))

    edges.sort(key=lambda edge: edge[2])

    parent = {node: node for node in graph}
    rank = {node: 0 for node in graph}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            if rank[root1] < rank[root2]:
                parent[root1] = root2
            elif rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root2] = root1
                rank[root1] += 1

    mst_edges = []
    total_weight = 0
    for u, v, weight in edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, weight))
            total_weight += weight

    return mst_edges, total_weight

# Define graph
graph = {
    1: {2: 4, 5: 1, 7: 2},
    2: {1: 4, 3: 7, 6: 5},
    3: {2: 7, 4: 1, 6: 8},
    4: {3: 1, 6: 6, 7: 4, 8: 3},
    5: {1: 1, 6: 9, 7: 10},
    6: {2: 5, 3: 8, 4: 6, 5: 9, 9: 2},
    7: {1: 2, 4: 4, 5: 10, 9: 8},
    8: {4: 3, 9: 1},
    9: {6: 2, 7: 8, 8: 1}
}

# User input for the root node
root_node = int(input("\nEnter the root node for Prim's algorithm: "))

prim_result_edges, prim_total_weight = prim_mst_dict(graph, root_node)
kruskal_result_edges, kruskal_total_weight = kruskal_mst_dict(graph)

# Display results
print("\nPrim's Algorithm MST:")
for edge in prim_result_edges:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")
print(f"Total weight of MST: {prim_total_weight}")

print("\nKruskal's Algorithm MST:")
for edge in kruskal_result_edges:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")
print(f"Total weight of MST: {kruskal_total_weight}")