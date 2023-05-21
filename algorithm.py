## project is based on recusion ##

############ RECUSION ############
# what is recurtion 

# recurtion is an algorithm design that call its self repeatedly in other to solve a particular problem until a condition is fullfiled.
# we have two proceduce in solving a recusion which is,
# Two processes of using a recurtion: 
# the base case: the base case tells the program when to terminate, the recurtion will stop once a condition is met.

# the recusive case: where a recusive case will continue to call its self towards a based criteria.

# now we look at the pythonic implementation of solving a recution.

# A physical world example would be to place two parallel mirrors facing each other. Any object in between them would be reflected recursively.


# we will be runing some code To implement it 

# we create a function so it could call itself

def recursion_fun(n):   # we will be using numbers to explain how recursion 
    # now we pass the condition that will sequencally solve the problem
    if n == 0:
        return 0 # or u can use the print function to til the user that it can call the program 
    
    else:
        # now we implement the rule to the recursion as the name implise
        result = n*(n-1)
        print(f"the recursion number is: {result}")
#  now we will call the function. we can all so take an input from the user
user = int(input("enter a number:\n"))

recursion_fun(user)

#  this is the end of the program and at this point i clearly understand the use of recursion.