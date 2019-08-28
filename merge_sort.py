def merge_sort (A) :
	if len(A)>1 :
		mid=len(A)//2
		left=A[:mid]
		right=A[mid:]

		merge_sort(left)
		merge_sort(right)

		i=j=k=0

		while i<len(left) and j <len(right) :
			if left[i]<right[j] :
				A[k]=left[i]
				i+=1
			else :
				A[k]=right[j]
				j+=1
			k+=1

		while i<len(left) :
			A[k]=left[i]
			i+=1
			k+=1
		while j<len(right) :
			A[k]=right[j]
			k+=1
			j+=1


A=[23,45,12,22,44,55]
print("unsorted array : ",A)
merge_sort(A)
print("Sorted array : ",A)
	
