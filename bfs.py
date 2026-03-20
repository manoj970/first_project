def bfs(graph , start):
    visited  = []
    queue    = []
    order    = []
    queue.append(start)
    visited.append(start)
    while queue:
        current = queue.pop(0)
        order.append(current)
        for i in graph:
            if i  not in visited:
                visited.append(i)
                queue.append(i)
    return order  
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(bfs(graph , 'A'))

from collections import deque
def bfs(graph , start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                queue.append(i)
    return order            
print(bfs(graph , 'B'))
          

