a=int(input("Enter the 1st number for multiplier "))
b=int(input("Enter the 2nd number for multiplier "))
try:
    c=a**b
    print("C is ",c)
except:
    print("Error: Exponent failed due to invalid inputs")
else:
    print("The exponent was successful")