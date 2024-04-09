#All statements are used only inside a loop
#Break
count=1
while count <=10:
    print(count)
    if(count==6):
        break
    count+=1
print("End")
#Continue
count=0
while count<10: 
    count+=1
    if count==5:
        continue
    print(count)
print("End")
#Pass is not a loop control statement,it is only used to pass(skip) any block without statement
count=1
while count <=10:
    if(count%2!=0):
        pass
    else:
        print(count)
    count+=1
print("End")

