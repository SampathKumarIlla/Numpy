def findsum(*args):

    sm = 1
    for i in args:
        sm *= i
    return sm

#Driver's code
z = findsum(1,2,3,4,5)
print(z)
