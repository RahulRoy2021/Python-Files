'''lst=[1,2,3,4,5]
print(lst)
print(lst[0:3:1])
for i in range(0,5):
    print(lst[i])
'''
lst=[]
num=int(input("Enter the no of elements you want to store"))
print("Enter the list elements")
for i in range(num):
    el=int(input())
    lst.append(el) #To add more element at the end of a list
print(lst)