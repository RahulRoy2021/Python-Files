tup=(1,2,3,4,5,6)
print(len(tup))#Length Function
#Repetition
print(tup*4)
#Concatenation
tup1=(7,8,9)
print(tup+tup1)
#Iteration
for i in tup+tup1:
    print(i)
#Comprehension
tup3=tuple(x for x in range(10,16) if x%2==0)
print(tup3)
#Membership
print(11 in tup3)
#Functions:
#MIN AND MAX:
print(min(tup),max(tup))
#COUNT:
print(tup.count(5))
#INDEX:
print(tup.index(5))
#SORTING:
print(tuple(sorted(tup)))
#By default ascending order
print(tuple(sorted(tup,reverse=True)))