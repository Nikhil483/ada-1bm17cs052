class Square_Root :
	def __init__(self,n) :
		self.n=n
		self.first=1
		self.last=self.n/2
		
	def calculate_root (self) :
		if n==0 or n==1 :
			return n
		while self.first<=self.last :
			mid=(self.first+self.last)//2
			if mid*mid==self.n :
				result=mid
				break
			elif mid*mid <self.n :
				self.first=mid+1
				result=mid
			else :
				self.last=mid-1
				
		return result
		
n=int(input("enter the element : "))	
element = Square_Root(n)
print(round(element.calculate_root()))


