class bubble_sort :
    def __init__(self,A,k) :
        self.A=A
        self.k=k
        
    def sorting(self) :
        for i in range(self.k): 
            for j in range(0, len(self.A)-i-1): 
                if self.A[j] > self.A[j+1] : 
                    self.A[j], self.A[j+1] = self.A[j+1], self.A[j]
                
    def print_k(self) :
        print("largest",str(k),"elements of the array are :",self.A[-self.k:])
        

A = [78,45,12,65,52,13,23] 
print("the list is : " ,A)
k=int(input("enter the value of k : "))
min_array=bubble_sort(A,k)
min_array.sorting()
min_array.print_k()
