# Patick Corcoran
# Ask user to input any positive integer.
# Output value, if even divide it by two.
# If value is odd multiply by three and add one.

p = int (input("Please enter any positive integer:"))
print (p)

while p > 1:
    if p % 2 == 0:
        p = p / 2
    else:    
        p = p * 3 + 1
    print (p)
