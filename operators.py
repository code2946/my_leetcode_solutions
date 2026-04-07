age= int(input("enter yourage : "))
if(age%2==0):
    print("that is an even number")
if (age>=18):
    print("you are above the age of consent")
elif(age<0):
    print("you have entered invalid age"  ) 
else:
   print(" you are underage")       