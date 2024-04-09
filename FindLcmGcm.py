import math
n1 = int(input("Enter n1 value:"))
n2 = int(input("Enter n2 value:"))
if n1<n2:
    greater=n2
else:
    greater=n1
while greater!=0:
    if(greater%n1==0 and greater%n2==0):
        lcm=greater
        break
    greater+=1
print("{0} is the lcm".format(lcm))
gcd=math.gcd(n1,n2)
print("{0} is the gcd".format(gcd))