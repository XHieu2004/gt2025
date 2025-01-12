class PathFinder:
    def __init__(self):
        self.adjacency_map = {}
    
    def add_connection(self, source, destination):
        """Add a one-way connection between nodes"""
        if source not in self.adjacency_map:
            self.adjacency_map[source] = []
        self.adjacency_map[source].append(destination)
    
    def find_path(self, origin, destination, max_depth=10):  #IDS

        def depth_limited_search(current, target, depth, visited):
            if depth < 0:
                return False
            if current == target:
                return True
            if current in visited:
                return False
            
            visited.add(current) # Mark current node as visited
            
            for next_node in self.adjacency_map.get(current, []): # Check all neighbors within depth limit
                if depth_limited_search(next_node, target, depth - 1, visited.copy()):
                    return True
            
            return False
        
        for depth in range(max_depth):  # Try deeper searches
            if depth_limited_search(origin, destination, depth, set()):
                return True
        return False

def main():
    network = PathFinder()
    
    # Test case
    test_edges = [
        ('1', '2'),
        ('2', '5'),
        ('3', '6'),
        ('4', '6'),
        ('4', '7'),
        ('6', '7')
    ]
    
    for start, end in test_edges:
        network.add_connection(start, end)
    
    try:
        start = input("Start node: ").strip()
        end = input("End node: ").strip()
        
        if network.find_path(start, end):
            print(f"=> Path exists between {start} and {end}.")
        else:
            print(f"=> No path exists between {start} and {end}.")
            
    except ValueError:
        print("Please enter valid node numbers.")

if __name__ == "__main__":
    main()