def node_is_valid( i, j, visited): 
	return (i >= 0 and i < row and 
                j >= 0 and j < col and 
                not visited[i][j] and graph[i][j]) 

def DFS( i, j, visited): 
        rowindex = [-1, -1, -1,  0, 0,  1, 1, 1]; 
        colindex = [-1,  0,  1, -1, 1, -1, 0, 1]; 
        visited[i][j] = True
        for k in range(8): 
            if node_is_valid(i + rowindex[k], j + colindex[k], visited): 
                DFS(i + rowindex[k], j + colindex[k], visited) 
  
def no_of_islands(): 
        visited = [ [False for j in range(col)] for i in range(row)] 
        count = 0
        for i in range(row): 
            for j in range(col):  
                if visited[i][j] == False and graph[i][j] == 1:  
                    DFS(i, j, visited) 
                    count += 1
        return count 
   
graph = [[0 for i in range(5)] for j in range(5)]
visited = [0]*5
n = 5

for i in range(n):
    for j in range(n):
        t = int(input())
        graph[i][j] = t
    visited[i] = 0 
   
row = len(graph) 
col = len(graph[0])  
print ("Number of islands is:")
print (no_of_islands()) 
