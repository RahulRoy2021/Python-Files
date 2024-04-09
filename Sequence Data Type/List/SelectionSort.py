lst=[] #Empty List
choice=1
while choice!=0:
    l=int(input("Enter the element :"))
    lst.append(l)
    choice=int(input("Enter your choice :"))
print(lst)
length=len(lst)
for i in range(length):
    min=lst[i]
    for j in range(i+1,length):
        if min>=lst[j]:
            min=lst[j]
            min_ind=j
    if min!=lst[i]:
        (lst[min_ind],lst[i])=(lst[i],min)
print(lst)
