lst=[]
def append(r):
    n=int(input("Enter the value you wnat to store"))
    r.append(n)
    print(r)
def remove(r):
    i=int(input("Enter the index"))
    del r[i]
    #r.remove(Element)
    print(r)
def insertele(r):
    i=int(input("Enter the index"))
    n=int(input("Enter the value you wnat to insert"))
    r.insert(i,n)
    print(r)
def copylist(r):
    mylist=r.copy()
    print(mylist)
def countele(r):
    ele=int(input("enter the element"))
    print("The element is {0} times in the list".format(r.count(ele)))
def sorting(r):
    r.sort()#Sort ascending by default
    print(r)
def reverselist(r):
    r.reverse()
    print(r)
def clearlist(r):
    r.clear()
    print(r)
def sumoflist(r):
    print(sum(r))
while True:
    choice=int(input("Enter your choice:\
         \n1.Append\n2.Remove\n3.Insert\n4.Copy\n5.Count\n6.Sort\n7.Reverse\n8.Clear\n9.Sum\n"))
    match choice:
        case 1:
            append(lst)
        case 2:
            remove(lst)
        case 3:
            insertele(lst)
        case 4:
            copylist(lst)
        case 5:
            countele(lst)
        case 6:
            sorting(lst)
        case 7:
            reverselist(lst)
        case 8:
            clearlist(lst)
        case 9:
            sumoflist(lst)
        case unknown_command:
            print("{0} is not valid input".format(unknown_command))
            break