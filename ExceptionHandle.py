a=int(input("Enter divident number"))
b=int(input("Enter divisor number"))

try:
    c=a/b
    print("Quetient is:",c)
except:
    print("Error: Division by zero is not allowed")
    