#Cat3 - Algorithm Based Problem 1 

#Initializing variables 
T = 0
X = 0 
notes = 0
coins = 9
#Taking input for number of test cases 
T = int(input("Please enter the number of test cases: "))

#Validation Check 
if T < 0 or T > 1000:
    #printing error message and requesting for input... 
    if T < 0: 
        print ("A minimum of 1 test case is required")
    else: 
        print ("A maximum of 1000 test cases only is permitted")
    while T < 0 or T > 1000:
        T = int(input("Please re-enter"))
#Starting the test case
for i in range (0,T):
    print ("-"*50)
    print ("")
    print ("Test Case #", i+1)
    #Taking the amount to pay by Chef as input 
    X = int(input("Please enter the amount (in rupees) which you wish to pay:"))
    #Processing
    if X >= 10: 
        notes = X/10 
        coins = X%10
    else: 
        coins = X
    print ("-"*50)
    print ("")
    #printing the output
    print ("No. of coins that could be used: ", coins)
    print ("-"*50)
