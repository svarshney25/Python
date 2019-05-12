print("___________________________________________________________________________________")

def hello_world():
    print("Hello World!")

# Call the function 
hello_world()

print("___________________________________________________________________________________")

def foo(x):                # x is a function parameter 
    print("x = " + str(x))

foo(5)      # pass to foo(). Here 5 is an argument passed to function foo

def square (x):
    print(x ** 2)

square(4)
square(8)
square(15)
square(23)
square(42)

print("__________________________________________________________________________________")

def sum_two_numbers(a,b):
    return a + b            # Return results to the function caller 

c = sum_two_numbers(3,12)   # Assign result of function execution to variable 'c'

def fib(n):
    result = []
    a = 1
    b = 1 
    while a < n: 
        result.append(a)
        tmp_var = b
        b=sum_two_numbers(a,b)
        a=tmp_var
    return result

print(fib(10))
print("_______________________________________________________________________________________")

# This code is only using a loop
result = 0
for x in range(5):
    v=x+1
    print("v=",str(v))
    result=result+v
    print(result)

# This code has the exact same result as above except it has a loop inside a function  
def AddTo(n):
    result = 0
    for x in range(n):
        v=x+1
        print("v=",str(v))
        result=result+v
        print(result)
    return result 

print("AddTo 100", str(AddTo(100)))

def

