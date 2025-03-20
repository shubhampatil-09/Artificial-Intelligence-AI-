//To implement Best First Search to find goal node//


tree={'A':[('B',12),('C',4)],'B':[('D',7),('E',3)],'C':[('F',8),('G',2)],'D':[],'E':[('H',0)],'F':[('H',0)],'G':[('H',0)],'H':[]}
start=input("Enter the start state: ")
goal=input("Enter the goal state: ")
open=[]
close=[]
def Bfs(start,goal,tree):
    if start not in close:
        print(start)
        close.append(start)
        neighbour=tree[start]
        for i in neighbour:
            if i[0][0] not in open:
                open.append(i)
    open.sort(key=lambda x:x[1])
    if open[0][0]==goal:
        print(open[0][0])
    else:    
       node=open[0]
       open.remove(node)
       Bfs(node[0],goal,tree)
Bfs(start,goal,tree)

