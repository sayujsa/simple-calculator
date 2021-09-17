def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
    
answer = "yes"
num1 = None

operations = {
"+" : add,
"-" : subtract,
"*" : multiply,
"/" : divide,    
}


while answer == "yes":
    if num1 == None:
        num1 = int(input("Enter first number : "))
        print("")
        
        for x in operations:
            print(x)
            
        action = input("Enter operation: ")
        num2 = int(input("\nEnter second number : "))
        
    else:
        for x in operations:
            print(x)
            
        action = input("Enter operation: ")
        num2 = int(input("Enter number : "))
        
    print("\nAnswer is : "+str(operations[action](num1,num2))+"\n")
    answer = input("Keep calculating? (yes/no) : ")
    solution = operations[action](num1,num2)
    num1 = solution
    
    
print("\nGood Bye")
