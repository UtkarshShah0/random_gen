import time
a=int(input("Enter The Lower Limit: "))
b=int(input("Enter The Upper Limit: "))
c=int(a + int(time.time()*1000) % (b-a))
print("The Random Generated Number is: ",c)
