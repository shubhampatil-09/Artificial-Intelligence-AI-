//To implement BFS traversal using queue // 

tree = {'A':['B','C'],'B':['D'],'C':['E'],'D':['F'],'E':['F'],'F':[]} 
 
def bfs_traversal(tree) : 
    start = input("Enter the start state :") 
    open = [start] 
    close = [] 
    while open: 
        node = open.pop(0) 
        if node not in close: 
            close.append(node) 
            neighbour = tree[node] 
             
            for i in neighbour: 
                open.append(i) 
    return close 
print("BFS traversal is :",bfs_traversal(tree)) 

