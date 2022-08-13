#Cat 3 - Algorithm Based Problem 2

#Initializing variables 
T = 0
X = 0 
Y = 0 

#Taking input of test cases
T = int(input("Enter number of test cases : "))
if T < 0 or T > 1000:
    #printing error message and requesting for input... 
    if T < 0: 
        print ("A minimum of 1 test case is required")
    else: 
        print ("A maximum of 1000 test cases only is permitted")
        while T < 0 or T > 1000:
            T = int(input("Please re-enter"))

for i in range (0,T):
    print ("Test Case #", i+1)
    #Taking input of Bob and Alice's heights 
    X = int(input("Enter Alice's height: "))
    if X < 100 or X > 200:
        print ("Alice's height must be greater than 100 and less than 200")
        while X < 100 or X > 200:
            X = int(input("Please re-enter: "))
    Y = int(input("Enter Bob's height: "))
    if Y < 100 or Y > 200:
        print ("Bob's height must be greater than 100 and less than 200")
        while Y < 100 or Y > 200:
            Y = int(input("Please re-enter: "))

    #Checking if Alice value = Bob value 
    if X == Y: 
        print ("Their heights cannot be equal")

        #Error message printed and re-entry process 
        while X == Y: 
            X = int(input("Please re-enter Alice's height: "))
            Y = int(input("Please re-enter Bob's height: "))
    
    
    #Processing 
    if X > Y: 
        print ("A")
    else: 
        print ("B")

