 
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
goal = input("Enter goal state :") 
def bfs(tree): 
 open = [start] 
 close = [] 
 if start == goal: 
     print("Start itself is the goal node") 
     return open 
 close.append(start) 
 while open:  
     node = open.pop(0) 
     neighbour=tree[node] 
     for i in neighbour: 
         close.append(i) 
         open.append(i) 
         if i == goal: 
             return close 
 print("Goal node does not exist") 
print("Traversal is ",bfs(tree))