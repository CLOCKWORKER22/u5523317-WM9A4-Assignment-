def add(a, b):
    return a + b
    
def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
    
def calculator():
    print("select type of operation:")
    print("1 add")
    print("2 subtract")
    print("3 multiply")
    print("4 divide")

    choice = input("Enter choice (1/2/3/4):")
    a = float(input("enter first number:"))
    b = float(input("enter second number:"))

choice = input()

if choice == "1/2/3/4":
print(add(a, b))
elif: print(sub(a, b))
elif: print(multiply(a, b))
eles: print(divide(a, b))

calculator()


