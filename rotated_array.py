import sys

class rotated_array :
	def __init__(self,A,key) :
		self.key=key
		self.A=A
		self.first=0
		self.last=0
		self.found=False

	def findMin(self,low, high): 
		if high <low: 
			return self.A[0] 
		if self.A[high] == self.A[low]: 
			return self.A[low] 

		mid = int((low + high)/2) 
		  
		if mid < high and self.A[mid+1] < self.A[mid]: 
			return self.A[mid+1] 
		  
		if mid > low and self.A[mid] < self.A[mid - 1]: 
			return self.A[mid] 
		if self.A[high] > self.A[mid]: 
			return findMin(self.A, low, mid-1) 
		return findMin(self.A, mid+1, high)
	
	def allocate_first_last(self) :
		mini=self.findMin(0,len(self.A)-1)

		min_index=self.A.index(mini)
		print("no of rotation : ",min_index)
		
		if(self.key==mini) : 
			print("element found at",str(min_index),"position")
			self.found=True
			exit()
		elif(self.key==self.A[-1]) : 
			print("element found at",str(len(self.A)-1),"position")
			self.found=True
			exit()
		elif self.key<self.A[-1] :
			self.first=min_index+1
			self.last=len(A)-1
		else :
			self.first=0
			self.last=min_index+2

	def binary_search (self) :
		while self.first <= self.last :
			mid=(self.first+self.last)//2
			if self.key==self.A[mid] :
				print("element found at",str(mid),"position")
				self.found=True
				break
			elif self.key<mid :
				self.first=mid+1
			else :
				self.last=mid-1
		if(self.found==False) :
			print("element not found")



A=[50,60,70,10,20,30,40]
print("The current list is  : ",A)
key=int(input("enter the key you want to search : "))
test_case=rotated_array(A,key)
test_case.allocate_first_last()
test_case.binary_search()

