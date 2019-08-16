with open('test1.txt') as f:
        test_cases=f.readlines()

for i in range(len(test_cases)) :
        test_cases[i]=test_cases[i].rstrip("\n").strip(). split(" ")
n=0

no_of_test_cases=len(test_cases)//3
for i in range(n,len(test_cases),3) :
        start_index=0
        last_index=0
        test_list=test_cases[i+1]
        test_list=list(map(int,test_list))
        key=list(map(int,test_cases[i+2]))[0]
        first=0
        last=len(test_list)
        mid=0
        while first<=last :
            mid=(first+last)//2
            if key==test_list[mid] :
                           for i in range(1,mid):
                              done=0
                              if key==test_list[mid-i] :
                                    start_index=start_index+1
                                    done=1
                              if key==test_list[mid+i] and mid+i < len(test_list):
                                    last_index=last_index+1
                                    done=1
                              if done==0: 
                                print("breaking out of loop")
                                break
                                
            elif test_list[mid]<key :
                first=mid+1
            else :
                last=mid-1
        print("start_index : ",mid-start_index)	
        print("last_index : ",mid+last_index)
        print("count :" ,start_index+last_index+1)