list=[]
num=int(input("Enter the number of elements in list:"))
for x in range(0,num):
    element=int(input("Enter element " + str(x+1) + ":"))
    list.append(element)
temp=list[0]
list[0]=list[num-1]
list[num-1]=temp
print(list)
