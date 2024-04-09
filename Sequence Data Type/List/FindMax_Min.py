lst=[] #Empty List
choice=1
while choice!=0:
    l=int(input("Enter the element :"))
    lst.append(l)
    choice=int(input("Enter your choice :"))
print(lst)
length=len(lst)
min=lst[0]
min_ind=0
for i in range(1,length):
    if min<lst[i]:
        pass
    else:
        min_ind=i
print("Minimum",lst[min_ind])