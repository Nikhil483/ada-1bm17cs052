tasks=[[0,1],[4,0],[4,1],[2,4],[3,4],[5,3],[5,2]]
n=6
#tasks=[[1,0],[2,0],[3,1],[3,2]]
#n=4
#tasks=[[0,3],[2,0],[1,2],[0,1]]
#n=4
arr=[[0]*(n) for x in range(n)]
li=[]

for val in tasks:
	arr[val[0]][val[1]]=1
for i in range(len(arr)) :
	if not sum(arr[i]) :
		continue
	for j in range(len(arr)) :
		if j not in li :
			indegree=sum(arr[j])
			if indegree: continue
			if indegree==0 :
				li.append(j)
				for a in range(len(arr)) :
					arr[a][j]=0
					
if len(li)!=n : print([])
else : print(li)
