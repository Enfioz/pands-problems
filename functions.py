# Practice functions

def degrees(sides):
    return (sides-2)*180

print("Sum of Internal Angles")

for s in range(3,9):
    d = degrees(s)
    print(str(s) + "sides: " + str(d))



