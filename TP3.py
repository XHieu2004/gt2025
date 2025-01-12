from collections import defaultdict

class TreeTraversal:
    def __init__(self):
        # Store the tree structure
        self.tree = defaultdict(list)
        # Track visited nodes 
        self.visited = set()

    #Add a directed edge from parent to child    
    def add_edge(self, parent, child):
        self.tree[parent].append(child)

    #Perform inorder traversal starting from given node    
    def inorder_subtree(self, node):
        if node not in self.tree:  # Leaf node
            print(node, end=' ')
            return
            
        children = sorted(self.tree[node])  # Sort children for consistent output
        
        # Process first child 
        if len(children) > 0:
            self.inorder_subtree(children[0])
            
        # Process root
        print(node, end=' ')
        
        # Process remaining children
        for child in children[1:]:
            self.inorder_subtree(child)

def main():
    tree = TreeTraversal()
    
    # Tes case
    edges = [
        (1, 2), (1, 3),
        (2, 5), (2, 6),
        (3, 4),
        (4, 8),
        (5, 7)
    ]
    
    for parent, child in edges:
        tree.add_edge(parent, child)
    
    # Get input node
    try:
        start_node = int(input("Enter the root node for subtree traversal: "))
        
        print(f"\nInorder traversal of subtree starting from node {start_node}:")
        tree.inorder_subtree(start_node)
        print()  
        
    except ValueError:
        print("Please enter valid node number")
        
if __name__ == "__main__":
    main()