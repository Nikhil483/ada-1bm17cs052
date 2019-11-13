def prim(n) :
    u,v=0,0
    ne,mincost=0,0
    elec=[1]*(n+1)
    while ne!=n-1 :
        mini=999999
        for i in range(n) :
            for j in range(n) :
                if elec[j]==1 :
                    if c[i][j]==1 :
                        mini=c[i][j]
                        u,v=i,j

        if elec[v] == 1 :
            print(u,"---",v," = ",mini)
            elec[v]=0
            ne+=1
            mincost+=mini

        c[u][v],c[v][u]=999999,999999
    print("mini cost" ,mincost)

'''c=[[0]*20]*20
n= int(input("enter the number of matrix : "))
print("enetr matrix : ")
for i in range(1,n+1) :
    for j in range(1,n+1) :
        c[i][j]=int(input())

'''
c=[[0,2,3,0,0],[2,0,0,0,6],[3,0,0,5,0],[0,4,5,0,0],[0,6,0,0,0]]
n=5
prim(n)
    
