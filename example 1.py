def hello():
    print("Hello")
    print("Programming is fun!")

def print_func(i, j = 100):
    d=i-j
    print(d)

def func5():
    global x
    x = 20
    print(x)
    
def func6():
    print(x+1)
  
def square1(x):
    return x * x

def square2(x):
    print( x * x)

def strange_function(n):
    if(n % 2 == 0):
        return True
    else:
        return False

print(strange_function(6))
print(strange_function(5))
print(strange_function(4))
##
##s=square1(4)+square1(5)
##print(s)
##print(square1(5))
##square2(4)




##func5()
##print(x)
##
##hello()
##
##a=float(input("Give first number"))
##b=float(input("Give second number"))
##
##print_func(a, b)


