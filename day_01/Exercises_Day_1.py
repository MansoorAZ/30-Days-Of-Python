    ### Exercise: Level 2
'''    
    1. Create a folder named day_1 inside 30
DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. 
Remember to use *print()* when you are working on a python file. Navigate to the directory where you have saved your file, and run it.
''' 
    # Day 1 - 30DaysOfPython Challenge
    
    print(2 + 3)             # addition(+)
    print(3 - 1)             # subtraction(-)
    print(2 * 3)             # multiplication(*)
    print(3 / 2)             # division(/)
    print(3 ** 2)            # exponential(**)
    print(3 % 2)             # modulus(%)
    print(3 // 2)            # Floor division operator(//)
    
    # Checking data types
    print(type(10))          # Int
    print(type(3.14))        # Float
    print(type(1 + 3j))      # Complex number
    print(type('blank'))  # String
    print(type([1, 2, 3]))   # List
    print(type({'name':'blank'})) # Dictionary
    print(type({9.8, 3.14, 2.7}))    # Set
    print(type((9.8, 3.14, 2.7)))    # Tuple
    
    ### Exercise: Level 3  
#1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
    
    print(type(1)) # Integer
    print(type(3.14159265)) #Float
    print(type(3 + 2j)) #Complex
    print(type("I am text"))#String
    print(type(False)) #Boolean
    print(type(['A', 'B', 'C'])) #List
    print(type({17.6, 2, 15.55})) # Set
    print(type((1,2,3,4,5,6,7,8,9,True))) #Tuple
    
#1. Find an [Euclidian distance] between (2, 3) and (10, 8)
    
#Answer:
euclidian_disctance = (10-2)**2 + (8-3)**2
euclidian_disctance**= 0.5
print(euclidian_disctance)
