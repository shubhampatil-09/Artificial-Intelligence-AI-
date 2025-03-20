// To implement DFS traversal using queue //
tree = { 
    'A' : ['B','C'], 
    'B' : ['D','E'], 
    'D' : [], 
    'E' : [], 
    'C' : ['F','G'], 
    'F' : [], 
    'G' : [] 
    } 
 
start = input("Enter start state :") 
def dfs_traversal(tree): 
visited = [] 
stack = [start] 
           while stack: 
           node = stack.pop() 
           if node not in visited: 
           visited.append(node) 
           neigbour = tree[node] 
           for i in neigbour: 
             stack.append(i) 
           return visited 
print("Traversal is ",dfs_traversal(tree))