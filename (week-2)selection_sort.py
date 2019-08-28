class selection_sort :
    def __init__(self,A,k) :
        self.A=A
        self.k=k
        
    def sorting(self) :
        for i in range(self.k): 
            mini = i 
            for j in range(i+1, len(self.A)): 
                if self.A[mini] > self.A[j]: 
                    mini = j 
            self.A[i], self.A[mini] = self.A[mini], self.A[i]
        
    def print_k(self) :
        print("Smallest",str(k),"elements of the array are :",(self.A[:k]))
        

A = [78,45,12,65,52,13,23] 
print("The list is : ",A)
k=int(input("enter the value of k : "))
min_array=selection_sort(A,k)
min_array.sorting()
min_array.print_k()
