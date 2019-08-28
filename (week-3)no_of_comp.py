
class bubble_sort :
    def __init__(self,A) :
        self.A=A
        self.count=0
        
    def sorting(self) :
        for i in range(len(self.A)): 
            for j in range(0, len(self.A)-i-1): 
                if self.A[j] > self.A[j+1] :
                    self.count+=1 
                    self.A[j], self.A[j+1] = self.A[j+1], self.A[j]
                
    def print_k(self) :
        print("the number of comparision for bubble sort is " ,self.count)
        
class selection_sort :
    def __init__(self,A) :
	    self.A=A	
	    self.count=0
        
    def sorting(self) :
        for i in range(len(self.A)): 
            mini = i 
            for j in range(i+1, len(self.A)): 
                if self.A[mini] > self.A[j]: 
                    mini = j 
                    self.count+=1
            self.A[i], self.A[mini] = self.A[mini], self.A[i]
        
    def print_k(self) :
        print("the number of comparision for selection sort is " ,self.count)
flag=0
def merge_sort (A) :
  global flag
  if len(A)>1 :
    mid=len(A)//2
    left=A[:mid]
    right=A[mid:]

    merge_sort(left)
    merge_sort(right)

    i=j=k=0

    while i<len(left) and j <len(right) :
          if left[i]<right[j] :
            flag+=1
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
          


print("\nfor finding smallest k elements ",end="\n")
A = [78,45,12,23,56,89,1]
print("The list is : ",A)
min_array=selection_sort(A)
min_array.sorting()
min_array.print_k()
print()
A = [78,45,12,23,56,89,2]
print("for finding largest k elements ",end="\n")
print("The list is : ",A)
max_array=bubble_sort(A)
max_array.sorting()
max_array.print_k()
print()
A = [78,45,12,23,56,89,6]
merge_sort(A)
print("merge sort count is  : ",flag)



