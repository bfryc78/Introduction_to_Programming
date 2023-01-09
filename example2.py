def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False 
    return True

##for i in range(2, 21):
##    if is_prime(i ):
##        print(i , end=" ")

def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

#intro()
intro("Sean Connery")
##print()
##print("Hello")
##print("Hello", "BlaBla", sep="$", end=" ")
##print("Hello", end="*")
