# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.


def bigger(x, y):
    if x > y:
        return x
    return y


# Solution 2
print bigger(2, 7)


def bigger(x, y):
    if x > y:
        return x
    else:
        return y


print bigger(3, 2)

print bigger(3, 3)

# Solution 3


def bigger(x, y):
    if x > y:
        r = x
    else:
        r = y


print bigger(3, 3)

#print bigger(2,7)
# >>> 7

#print bigger(3,2)
# >>> 3

#print bigger(3,3)
# >>> 3
