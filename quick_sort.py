def partition (A,first,last) :
	i=first-1
	pivot=A[last]
	for j in range(first,last) :
		if A[j]<pivot :
			i+=1
			A[i],A[j]=A[j],A[i]
	A[i+1],A[last]=A[last],A[i+1]
	return i+1

def sort(A,first,last) :
	if first<last :
		pivot=partition(A,first,last)
		sort(A,first,pivot-1)
		sort(A,pivot+1,last)


A=[45,23,12,43,22,65]
print("unorted array : ",A)
sort(A,0,len(A)-1)
print("Sorted Array : ",A)

