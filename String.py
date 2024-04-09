Paragraph='''My name is Rahul Roy \
and recently i have joined into adamas univerity.'''#How to handle multi line character in a string
print(Paragraph)

Paragraph="""My name is Rahul Roy
and recently I have joined into adamas univerity"""#That is called delemeter
print(Paragraph)

#STRING OPERATIONS:
#String Concatenation
str1="MY NAME IS"
str2="RAHUL ROY"
str3=str1+" "+str2
print(str3)
#String Indexing
flavor="Chocolate"
print(flavor[0])#For printing the first element 
print(flavor[-1])#For printing the last element
#Find the last character of a string without using minus indexing
str4=len(flavor)-1
print(flavor[str4])
#String Slicing
print(flavor[0:4])#Extracting substring from position 1 to 4

#Strings are immutable
word="Goal"
#word[0]="f"
#print(word[0])That will show runtime error(TYPE ERROR)
print("F"+word[1:])
#String Functions:
#Converting string case
#UPPERCASE
print(word.upper())
#LOWERCASE
print(word.lower())
#Removing whitespace from a string
name="    Rahul Roy   "
print(name.strip())
print(name.lstrip())#for removing left side whitespace
print(name.rstrip())#for removing right side whitespace
#If a string starts or ends with a particular substring
print(str1.startswith("MY"))
print(str2.endswith("ROY"))
#Find substring's index in a string
print(name.find("Rahul"))
#Find the length of any string
print(len("Rahul"))
#Number to string conversion
no_of_pancakes=10
print("I love to eat "+str(no_of_pancakes)+" pancakes daily")
#Split Function
str5="Hello World"
print(str5.split(" "))
#Replace Function
print(str5.replace("World","Rahul"))