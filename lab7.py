#----DLS

# Graph representation
graph = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'K': ['N', 'M'],
    'D': ['G', 'C'],
    'E': ['H', 'I'],
    'I': ['L'],
    'F': [], 'J': [], 'N': [], 'M': [], 'G': [], 'C': [], 'H': [], 'L': []
}

# Depth Limited Search (Iterative)
def depth_limited_search(start, goal, limit):
    stack = [(start, [start], 0)]  # (node, path, depth)
    
    while stack:
        node, path, depth = stack.pop()
        
        if node == goal:
            return path
        
        if depth < limit:
            for neighbor in reversed(graph[node]):  
                stack.append((neighbor, path + [neighbor], depth + 1))
     
     
    return None

#-------------------iddfs---------------

# Graph representation
graph = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'K': ['N', 'M'],
    'D': ['G', 'C'],
    'E': ['H', 'I'],
    'I': ['L'],
    'F': [], 'J': [], 'N': [], 'M': [], 'G': [], 'C': [], 'H': [], 'L': []
}

# Iterative Deepening Search (using stack only)
def iterative_deepening_search(start, goal, max_depth):
    for limit in range(max_depth + 1):   #LIMIT =0,1,2,3,4
        stack = [(start, [start], 0)]   # (node, path, depth)
        
        while stack:
            node, path, depth = stack.pop()
            
            if node == goal:
                return path, limit   # return path + depth found
            
            if depth < limit:
                for neighbor in reversed(graph[node]):  
                    stack.append((neighbor, path + [neighbor], depth + 1))
    
    return None, 


# -------------------------------
# Run IDS
start, goal = 'A', 'G'
path, depth = iterative_deepening_search(start, goal, 5)

print("IDS Path:", path)
print("Found at Depth:",depth)
