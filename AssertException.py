def cube_root(num):
    # check if the number is positive and if not negative i would raise an exception
    assert(num>=0), "pass a positive number"
    return num**(1/3)

print(cube_root(8))


print(cube_root(-8))