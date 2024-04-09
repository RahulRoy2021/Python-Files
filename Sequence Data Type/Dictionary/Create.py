emp={'Name':'Rahul','Id':10,'Salary':40000}
print(emp)
print(emp['Name'])
#Get
print(emp.get('Name'))
#Keys
print(emp.keys())
#Items
print(emp.items())
#Values
print(emp.values())
#Pop
emp.pop("Id")
print(emp)
#Popitem for deleting last key:value pair
emp.popitem()
print(emp)
#Update
emp.update({"Name":'Riju'})
print(emp)
#Copy
emp1=emp.copy()
print(emp1)
#Set default for inserting new key or update value of a particular key
emp.setdefault("Age",20)
print(emp)
#Converts list to dictionary
lst=['Name','Age','Id']
lst1=['Rahul',20,10]
print(dict(zip(lst,lst1)))
#Clear
emp.clear()
emp1.clear()
print(emp)
print(emp1)
