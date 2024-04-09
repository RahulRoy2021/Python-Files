lst=[1,1,1,1,1,1,1,1,1]
def sumoflist(lst):
    if len(lst)==1:
        return lst[0]
    else:
        return lst[0]+sumoflist(lst[1:])
print(sumoflist(lst))