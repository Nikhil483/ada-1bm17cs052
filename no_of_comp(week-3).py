
class bubble_sort :
    def __init__(self,A,k) :
        self.A=A
        self.k=k
class bubble_sort :
    def __init__(self,A,k) :
        self.A=A
        self.k=k
        self.count=0
        
    def sorting(self) :
        for i in range(self.k): 
            for j in range(0, len(self.A)-i-1): 
                if self.A[j] > self.A[j+1] :
                    self.count+=1 
                    self.A[j], self.A[j+1] = self.A[j+1], self.A[j]
                
    def print_k(self) :
        print("largest",str(k),"elements of the array are :",self.A[-self.k:])
        print("the number of comparision for selection sort is " ,self.count)
        
class selection_sort :
    def __init__(self,A,k) :
	    self.A=A	
	    self.k=k
	    self.count=0
        
    def sorting(self) :
        for i in range(self.k): 
            mini = i 
            for j in range(i+1, len(self.A)): 
                if self.A[mini] > self.A[j]: 
                    mini = j 
                    self.count+=1
            self.A[i], self.A[mini] = self.A[mini], self.A[i]
        
    def print_k(self) :
        print("Smallest",str(k),"elements of the array are :",(self.A[:k]))
        print("the number of comparision for selection sort is " ,self.count)
        
print("\nfor finding smallest k elements ",end="\n")
A = [78,45,12,65,52,13,23] 
print("The list is : ",A)
k=int(input("enter the value of k : "))
min_array=selection_sort(A,k)
min_array.sorting()
min_array.print_k()
print()
print("for finding largest k elements ",end="\n")
A = [78,45,12,65,52,13,23] 
print("The list is : ",A)
k=int(input("enter the value of k : "))
max_array=bubble_sort(A,k)
max_array.sorting()
max_array.print_k()


        self.count=0
        
    def sorting(self) :
        for i in range(self.k): 
            for j in range(0, len(self.A)-i-1): 
                if self.A[j] > self.A[j+1] :
                    self.count+=1 
                    self.A[j], self.A[j+1] = self.A[j+1], self.A[j]
                
    def print_k(self) :
        print("largest",str(k),"elements of the array are :",self.A[-self.k:])
        print("the number of comparision for selection sort is " ,self.count)
        
class selection_sort :
    def __init__(self,A,k) :
	    self.A=A	
	    self.k=k
	    self.count=0
        
    def sorting(self) :
        for i in range(self.k): 
            mini = i 
            for j in range(i+1, len(self.A)): 
                if self.A[mini] > self.A[j]: 
                    mini = j 
                    self.count+=1
            self.A[i], self.A[mini] = self.A[mini], self.A[i]
        
    def print_k(self) :
        print("Smallest",str(k),"elements of the array are :",(self.A[:k]))
        print("the number of comparision for selection sort is " ,self.count)
        
print("\nfor finding smallest k elements ",end="\n")
A = [78,45,12,65,52,13,23] 
print("The list is : ",A)
k=int(input("enter the value of k : "))
min_array=selection_sort(A,k)
min_array.sorting()
min_array.print_k()
print()
print("for finding largest k elements ",end="\n")
A = [78,45,12,65,52,13,23] 
print("The list is : ",A)
k=int(input("enter the value of k : "))
max_array=bubble_sort(A,k)
max_array.sorting()
max_array.print_k()

