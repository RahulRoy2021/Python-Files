char=65
for i in range(0,4):
    for j in range(0,i+1,1):
        print(chr(char),end=(" "))
        char+=1
    print()