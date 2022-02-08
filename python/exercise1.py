name=input ("Enter your name: ")

age = input  ("Enter your age: ")

ale = input ("Enter your average life expectancy: " )
X = age
if  (age <  18):
    X = (18 - age)
print ("Student")
print ("At least " +X + "years to become a worker.")
else if (age < 65 ):
    X = (65 - age)
    print ("Worker")
    print (X +" years to retire")
else if (age >= 65):
     X = ale - age
     print ("Retired")
     print ( X + " years to die")
else
    print ("Already died")