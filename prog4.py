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
 
def dfs(tree): 
 open = [start] 
 close = [] 
 
 if start == goal: 
     print("Start itself is the goal node") 
     return open 
 
 while open:  
     node = open.pop() 
     neighbour=tree[node] 
     close.append(node) 
     for i in neighbour: 
         open.append(i) 
         if i == goal: 
             close.append(i) 
             return close 
 print("Goal node does not exist") 
 
print("Traversal is ",dfs(tree)) 