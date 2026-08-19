num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

print("\nChoose an operation:")
print("1. Addtion")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice= int(input("Enter your choice: "))

if choice==1:
    print("Addition:",num1 + num2)
elif choice==2:
    print("Subtraction:", num1 - num2)
elif choice==3:
    print("Multiplication:",num1 * num2)
elif choice==4:
    print("Divition:",num1 / num2)
else:
    print("Invalid choice")