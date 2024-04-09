line=input("Enter the line :")
sub=input("Enter the substring :")
length=len(line) #Length of the initial string
lensub=len(sub) #Length of the substring which needs to search
start=count=0 #Initializing the start and count with 0
end=length #Similarly initializing end with 0
while True:  #Make a infinite loop
    pos=line.find(sub,start,end) #Get the position of the substring(Start and end is the limit of the find function)
    if pos!=-1: #Checking condition whether the substring is present in that string or not
        count+=1 #Updating the count while getting any substring is present
        start=pos+lensub #Updating start after getting substring matched
    else:
        break # if the particular substing is not present in the string then the loop will not be executed anymore
    if start>=length: #if the start becomes greater than length then the loop will be broken
        break
print("No. of occurance of",sub,":",count)# printing the number of the occurance of the substring in the string

