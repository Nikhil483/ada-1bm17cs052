import collections
def bfs(graph, root): 
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue: 
        vertex = queue.popleft()
        print(vertex)
        for neighbour in graph[vertex]: 
            if neighbour not in visited: 
                visited.add(neighbour) 
                queue.append(neighbour)

graph = [1:[1,2,3],1:[4],3:[5],4:[1,2]]

bfs(graph)


