#takes graph as adjacency list i.e defualtdict(list)
#For an unidrected graph
def detectCycle(graph):
    stack = []
    visited = set()
    stack.append(graph[0], graph[0])

    while(stack):
        curr, parent = stack.pop()
        visited.add(curr)        
        
        for neighbour in graph[curr]:
            if(neighbour == parent):
                continue
            elif(neighbour in visited and neighbour != parent):
                return True
            else:
                stack.append( (neighbour, curr) )
                
    return False
