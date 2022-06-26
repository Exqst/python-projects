def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multi(x, y):
    return x * y

def divi(x, y):
    if y != 0:
        return x / y
    else:
        return "You cannot divide by 0"
    
def remain(x, y):
    if y != 0:
        return x % y
    else:
        return "You cannot divide by 0"

print("Select from the menu on what you would like to do: ")
print("1. Add")
print("2. Subtract")
print("3. Multiplication")
print("4. Dividision")
print("5. Modulo Division")

while True:
    choice = input("Enter your choice from the menu: ")
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == '1':
            print(num1, " + " , num2, " = ", add(num1,num2))
            
        elif choice == '2':
            print(num1, " - ", num2, " = ", sub(num1, num2))
            
        elif choice == '3':
            print(num1, " * ", num2, " = ", multi(num1, num2))
            
        elif choice == '4':
            print(num1, " / ", num2, " = " , divi(num1, num2))
        
        elif choice == '5':
            print(num1, " % ", num2, " = " , remain(num1, num2))
                
        loopers = input("Would you like to another calculation? (y/n): ")
        if loopers == "n":
            break
        
    else:
        print("Invalid Input")
        exit()
