# Enter positive floating-point number as input
# Output an approximation of its square root

from math import sqrt

def squareroot(x):
    return(sqrt(x))

x = float(input("Please enter a positive number: "))
ans = (sqrt(x))
y = format(ans, ".1f")

print("The square root of %s is approx." % x, y)

# push to github