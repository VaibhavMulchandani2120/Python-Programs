#Function With No Argument & No Return Values

def printLine():
    print("*"*50)

printLine()
print("Welcome To User Defined Function In Python.")
printLine()


#Function With Argument But No Return Values

def add(a,b):
    print("Addition :",a+b)

printLine()
add(10,25)


#Function With Argument and Return Values

def sub(a,b):
    return (a-b)

printLine()
ans=sub(10,20)
print("Subtraction : ",ans)
