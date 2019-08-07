class search :
	def __init__ (self):
		self.test_cases=[]
		self.n=1
		
	def read_file(self) :
		with open('test.txt','r') as f :
			self.test_cases=f.readlines()
			for i in range(len(self.test_cases)):
				self.test_cases[i]=self.test_cases[i].rstrip('\n')
		
	def searching_element(self,no_of_elements,key,test_list) :
		if key in test_list :
			print("1")
		else :
			print("-1")
		
		
	def allocate_key_and_search(self) :
		for i in range(self.n,len(self.test_cases)) :
			if i%2==1 :
				self.n=self.n+2
				test_list=self.test_cases[i+1]
				test_list=test_list.split(" ")
				for k in range (len(test_list)) :
					test_list[k]=int(test_list[k])
				param=self.test_cases[i]
				param=param.split(" ")
				no_of_elements=int(param[0])
				key=int(param[1])
				self.searching_element(no_of_elements,key,test_list)
				
#main part			
case = search()
case.read_file()
case.allocate_key_and_search()