def dfs(v):
    print(v)
    visited[v] = 1
    for i in range(n):
        if arr[v][i] and not visited[i]:
            dfs(i)

def connected():
    for i in range(n):
        if not visited[i]:
            dfs(i)
            print("\n")

arr = [[0 for i in range(5)] for j in range(5)]
visited = [0]*5
n = 5

for i in range(n):
    for j in range(n):
        t = int(input())
        arr[i][j] = t
    visited[i] = 0

connected()
