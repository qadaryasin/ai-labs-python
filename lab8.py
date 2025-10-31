#-------------GFBS---------------------------------
import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    open_list = [(heuristic[start], start, [start])]  # (priority, node, path)
    visited = set()

    while open_list:
        _, node, path = heapq.heappop(open_list) # will return the one with the minimum value as its min heap

        if node == goal:
            return path   # ✅ return path instead of just True

        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(open_list, (heuristic[neighbor], neighbor, path + [neighbor]))

    return None  # if no path found

graph = {
    'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
    'Sibiu': ['Fagaras', 'Rimnicu'],
    'Timisoara': ['Lugoj'],
    'Zerind': ['Oradea'],
    'Fagaras': ['Bucharest'],
    'Rimnicu': ['Pitesti'],
    'Pitesti': ['Bucharest'],
    'Bucharest': []
}

heuristic = {
    'Arad': 366, 'Sibiu': 253, 'Timisoara': 329, 'Zerind': 374,
    'Fagaras': 176, 'Rimnicu': 193, 'Pitesti': 100, 'Bucharest': 0
}

path = greedy_best_first_search(graph, 'Arad', 'Bucharest', heuristic)
print("Path:", path)




#-------------------------------A*---------------------------------------------------------------
import heapq

def a_star_search(graph, start, goal, heuristic):
    # OPEN list as a priority queue (f, g, node, path)
    open_list = [(heuristic[start],0, start, [start])]
    visited = {}  # stores best g cost for each node 0

    while open_list:
        f, g, node, path = heapq.heappop(open_list) #min based on f value

        # Goal check
        if node == goal:
            return path, g   # return path and cost

        # If we already found a cheaper way, skip
        if node in visited and visited[node] <= g:  #means that if we already have the cheapest path for that node and its being visited 
            #again and this time it costs more so skip this path we dont need it we already have the cheapest one so far for this node 
         continue #we start from while loop again
        visited[node] = g #other option if g is lesser this time then we add it to visited with this val and expland its neigbors

        # Expand neighbors
        for neighbor, cost in graph.get(node, []):
            new_g = g + cost
            new_f = new_g + heuristic[neighbor]
            heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')  # No path found

graph = {
    'Arad': [('Sibiu', 140), ('Timisoara', 118), ('Zerind', 75)],
    'Sibiu': [('Fagaras', 99), ('Rimnicu', 80)],
    'Timisoara': [('Lugoj', 111)],
    'Zerind': [('Oradea', 71)],
    'Fagaras': [('Bucharest', 211)],
    'Rimnicu': [('Pitesti', 97)],
    'Pitesti': [('Bucharest', 101)],
    'Bucharest': []
}

heuristic = {
    'Arad': 366, 'Sibiu': 253, 'Timisoara': 329, 'Zerind': 374,
    'Fagaras': 176, 'Rimnicu': 193, 'Pitesti': 100, 'Bucharest': 0
}

path, cost = a_star_search(graph, 'Arad', 'Bucharest', heuristic)
print("Optimal Path:", path)
print("Total Cost:", cost)





# 8 puzzle game


import heapq

# Heuristic: number of misplaced tiles
def misplaced_tiles(state, goal):
    return sum(1 for i in range(len(state)) if state[i] != 0 and state[i] != goal[i])

# Generate neighbors by sliding blank tile
def get_neighbors(state):
    neighbors = []
    idx = state.index(0)  # blank position
    x, y = divmod(idx, 3)

    moves = {
        'Up': (x-1, y),
        'Down': (x+1, y),
        'Left': (x, y-1),
        'Right': (x, y+1)
    }

    for move, (nx, ny) in moves.items():
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_idx = nx * 3 + ny
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append((tuple(new_state), move))
    return neighbors

# A* search for 8-puzzle
def a_star(start, goal):
    open_list = [(misplaced_tiles(start, goal), 0, start, [])]  # (f, g, state, path)
    visited = {}

    while open_list:
        f, g, state, path = heapq.heappop(open_list)

        if state == goal:
            return path, g  # solution path + cost

        if state in visited and visited[state] <= g:
            continue
        visited[state] = g

        for neighbor, move in get_neighbors(state):
            new_g = g + 1
            new_f = new_g + misplaced_tiles(neighbor, goal)
            heapq.heappush(open_list, (new_f, new_g, neighbor, path + [move]))

    return None, float("inf")

# -------------------------------
# Example usage
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)  # initial state

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)  # goal state

path, cost = a_star(start, goal)

print("Solution moves:", path)
print("Total moves required:", cost)# 8 puzzle game


import heapq

# Heuristic: number of misplaced tiles
def misplaced_tiles(state, goal):
    return sum(1 for i in range(len(state)) if state[i] != 0 and state[i] != goal[i])

# Generate neighbors by sliding blank tile
def get_neighbors(state):
    neighbors = []
    idx = state.index(0)  # blank position
    x, y = divmod(idx, 3)

    moves = {
        'Up': (x-1, y),
        'Down': (x+1, y),
        'Left': (x, y-1),
        'Right': (x, y+1)
    }

    for move, (nx, ny) in moves.items():
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_idx = nx * 3 + ny
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append((tuple(new_state), move))
    return neighbors

# A* search for 8-puzzle
def a_star(start, goal):
    open_list = [(misplaced_tiles(start, goal), 0, start, [])]  # (f, g, state, path)
    visited = {}

    while open_list:
        f, g, state, path = heapq.heappop(open_list)

        if state == goal:
            return path, g  # solution path + cost

        if state in visited and visited[state] <= g:
            continue
        visited[state] = g

        for neighbor, move in get_neighbors(state):
            new_g = g + 1
            new_f = new_g + misplaced_tiles(neighbor, goal)
            heapq.heappush(open_list, (new_f, new_g, neighbor, path + [move]))

    return None, float("inf")

# -------------------------------
# Example usage
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)  # initial state

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)  # goal state

path, cost = a_star(start, goal)

print("Solution moves:", path)
print("Total moves required:", cost)