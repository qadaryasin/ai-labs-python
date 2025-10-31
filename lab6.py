#  DFS

def DFS(graph, start, target):
        stack=[]
        visited = set()
        ordered_traversal = []

        stack.append(start)
        visited.add(start)
        while stack:
            node = stack.pop()
            print(f'Explroing {node}')
            if node == target:
                print(f'Node {node} found ...')
                break
            ordered_traversal.append(node)
            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)

        print("DFS traversal order:", ordered_traversal)

graph = {          #an adjacency list consisting of letters
        'A': ['B', 'F','D','E'],
        'B': ['A','K', 'J'],
        'C': ['E'],
        'D': ['A','G'],
        'E': ['A','C','H','I'],
        'F': ['A'],
        'G': ['D'],
        'H': ['E'],
        'I': ['L','E'],
        'J': ['B'],
        'K': ['B','N','M'],
        'L': ['I'],
        'M': ['K'],
        'N': ['K'],
    }

start_node = 'A'
print(f"BFS traversal starting from node '{start_node}':")
DFS(graph, start_node,target ='G')




#Task 1:

# Graph representation using dictionary
graph = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'K': ['N', 'M'],
    'J': [],
    'N': [],
    'M': [],
    'F': [],
    'D': ['G'],
    'G': [],
    'E': ['C', 'H', 'I'],
    'C': [],
    'H': [],
    'I': ['L'],
    'L': []
}

# Depth First Search using Stack
def dfs_stack(start, goal):
    stack = [start]       # stack for DFS
    visited = []          # to store visited nodes

    while stack:
        node = stack.pop()       # remove last element (LIFO)
        if node not in visited:
            print(node, end=" ") # visit node
            visited.append(node)

            if node == goal:
                print("\nGoal node found!")
                return

            # Add children to stack (in reverse to maintain order)
            for child in reversed(graph[node]):
                if child not in visited:
                    stack.append(child)
    print("\nGoal node not found!")

# Run DFS
dfs_stack('A', 'G')
