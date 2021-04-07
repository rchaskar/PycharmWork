'''def average(a,b):
    return (a+b/2)

print(average(20,10))

'''

'''def calculate(a,b):
    x=a+b
    y=a-b
    z=a*b
    r=a/b
    return x,y,z,r

print(calculate(10,20))
'''

#function inside another function
'''
def message(name):
    def gretting():
        return "How are u "
    return gretting() + name

print(message("Rahul "))

'''
'''
def display():
    def messsage():
        return "hello"
    return messsage()

print(display())



def display():
    def message():
        return "Hi!!"
    return message

fun=display()
print(fun())
'''

#python program to find a factorial of a given number

def factorial(n):
    if n==0:
     result=1
    else:
        result=n*factorial(n-1)

    return result

print(factorial(3))

