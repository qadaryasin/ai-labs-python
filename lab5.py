
#question 1(graph):

from collections import deque
class Graph:
    def __init__(self):
        self.adj_list={}
    

    def add_edge(self,u,v):
       if not u in self.adj_list:
         self.adj_list[u]=[]

       if not v in self.adj_list:
          self.adj_list[v]=[]

       self.adj_list[u].append(v)
       self.adj_list[v].append(u)

    def print_graph(self):
       for node in self.adj_list:
          print(f"{node}-->{self.adj_list[node]}")
    

    def BFS(self,start):
       queue=deque()
       visited=set()
       ordered_traversal=[]


       queue.append(start)
       visited.add(start)

       while queue:
          node=queue.popleft()
          print(f"EXploring {node}..")
          ordered_traversal.append(node)

          for neighbour in self.adj_list[node]:
             if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                    
       print("BFS traversal order :",ordered_traversal)




graph_obj=Graph()
graph_obj.add_edge(0,1)
graph_obj.add_edge(0,4)
#graph_obj.add_edge(1,0) no need to repeat Your add_edge(u, v) function already adds the edge in both directions
graph_obj.add_edge(1,4)
graph_obj.add_edge(1,3)
graph_obj.add_edge(1,2)
#graph_obj.add_edge(2,1)
graph_obj.add_edge(2,3)
#graph_obj.add_edge(3,1)
#graph_obj.add_edge(3,2)
graph_obj.add_edge(3,4)
#graph_obj.add_edge(4,0)
#graph_obj.add_edge(4,1)
#graph_obj.add_edge(4,3)

print("Adjacency List:")
graph_obj.print_graph()

print("\nBFS Traversal:")
graph_obj.BFS(0)


#question 2 (BFS):----------------------------------------------------------------------------------
from collections import deque

def BFS(graph , start):
    queue = deque()
    visited = set()
    ordered_traversal = []

    queue.append(start)
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(f'Exploring {node}...')
        ordered_traversal.append(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    print(f'visited in BFS : ' , ordered_traversal)


graph = {          #an adjacency list consisting of letters
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

start_node = 'A'
print(f"BFS traversal starting from node '{start_node}':")
BFS(graph, start_node)

#question 3(graph, finding target):---------------------------------------------------
from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def print_graph(self):
        for node in self.adj_list:
            print(f"{node} --> {self.adj_list[node]}")

    def BFS(self, start, target):
        queue = deque()
        visited = set()
        ordered_traversal = []

        queue.append(start)
        visited.add(start)
        while queue:
            node = queue.popleft()
            print(f'Explroing {node}')
            if node == target:
                print(f'Node {node} found ...')
                break
            ordered_traversal.append(node)
            for neighbour in self.adj_list[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        print("BFS traversal order:", ordered_traversal)



graph2 = Graph()
graph2.add_edge('A' , 'B')
graph2.add_edge('A' , 'F')
graph2.add_edge('A' , 'D')
graph2.add_edge('A' , 'E')
graph2.add_edge('B' , 'K')
graph2.add_edge('B' , 'J')
graph2.add_edge('K' , 'N')
graph2.add_edge('K' , 'M')
graph2.add_edge('D' , 'G')
graph2.add_edge('E' , 'C')
graph2.add_edge('E' , 'H')
graph2.add_edge('E' , 'I')
graph2.add_edge('I' , 'L')

print("Adjacency List:")
graph2.print_graph()
graph2.BFS('A' , target = 'G')

#question 4(priority queue):
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, priority,item):
        self.queue.append((priority, item))

    def dequeue(self):
        if self.is_empty():
            return None
        # Find the item with the highest priority (smallest number)
        self.queue.sort()  # sort by priority
        return self.queue.pop(0)[1]  # pop the priority(discard) and return only the item 

    def display(self):
        print("Priority Queue:")
        for priority, item in sorted(self.queue):
            print(f"{item} (Priority: {priority})")

# Example usage
pq = PriorityQueue()
pq.enqueue( 3,"Task A")
pq.enqueue( 1,"Task B")
pq.enqueue( 2,"Task C")

pq.display()

print("Dequeued:", pq.dequeue())
pq.display()





        
