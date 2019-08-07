class maximum:
    def __init__(self, test_list,maxi,n):
       self.test_list=test_list
       self.maxi=maxi
       self.n=n

       
    def take_input(self):
        
        for i in range (0,self.n) :
            a=int(input("enter the element "+str(i)+" :"))
            self.test_list.append(a)
        print(self.test_list)


    def calculate_max(self):
        for i in range (0,self.n) :
            if self.test_list[i]>self.maxi :
                self.maxi=self.test_list[i]
        print("the maximum value in the list is "+str(self.maxi))

        
        
list1 = maximum([],0,0)
list1.n= int(input("enter the number of elements : "))
print(list1.n)
list1.take_input()
list1.calculate_max()
