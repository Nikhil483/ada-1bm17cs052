class search:
	def __init__(self):
		self.test_cases=[]
		self.no_of_test_cases=0
		self.n=1
		
	def read_file(self,filename):
		with open(filename,'r') as f:
			self.test_cases=f.readlines()
			if f.close():
				print("file closed")
			for i in range(len(self.test_cases)):
				self.test_cases[i]=self.test_cases[i].rstrip('\n')
		self.no_of_test_cases=int(self.test_cases[0])

	def searching_element(self,no_of_elements,key,test_list) :
		if key in test_list:
			print("1")
		else:
			print("-1")

	def allocate_key_and_search(self):
		for i in range(self.n,len(self.test_cases)):
			if i%2==1 and self.no_of_test_cases>0:
				self.no_of_test_cases=self.no_of_test_cases-1
				self.n=self.n+2
				test_list=self.test_cases[i+1]
				test_list=test_list.split(" ")
				param=self.test_cases[i]
				param=param.split(" ")
				no_of_elements=int(param[0])
				if len(test_list)!= no_of_elements :
					print("wrong test case provided")
				else :
					for k in range (no_of_elements) :
						test_list[k]=int(test_list[k])
					key=int(param[1])
					self.searching_element(no_of_elements,key,test_list)

case = search()
case.read_file('test.txt')
case.allocate_key_and_search() 