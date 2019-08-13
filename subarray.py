class Max_subarray :
	def __init__(self) :
		self.test_list=[]
		self.final_subarray=[]
		self.test_subarray=[]
	
	def get_list(self) :
		self.test_list.append(input("enter the elements and s to stop : "))
		while self.test_list[-1]!="s" :
			self.test_list.append(input("enter the element : "))
		self.test_list.pop()
		self.test_list=list(map(int,self.test_list))
	
	def calculate_max_sum_and_subarray(self) :
		self.final_subarray.append(self.test_list[0])
		self.test_subarray.append(self.test_list[0])
		for i in range (1,len(self.test_list)) :
			self.test_subarray.append(self.test_list[i])
			if self.test_list[i] > sum(self.test_subarray) :
				self.test_subarray.clear()
				self.test_subarray.append(self.test_list[i])
			if sum(self.test_subarray) > sum(self.final_subarray) :
				self.final_subarray.clear()
				self.final_subarray=self.test_subarray[:]

		
array = Max_subarray()
array.get_list()
array.calculate_max_sum_and_subarray()
print("Subarray with max sum is",array.final_subarray)
print("Sum of the Maximaum subarray elemets is : ",sum(array.final_subarray))
