def cube_root(num):
    # check if the number is positive and if not negative i would raise an exception
    assert(num>=0), "pass a positive number"
    return num**(1/3)

num2=int(input("Enter a number "))
try:
    print("your cube root is: ",cube_root(num2))
except:
    print("Pleased pass positive number")

print("Hii. How are you")