# Patrick Corcoran
# Read a txt file.
# Output the number of e's it contains.

# Opens, reads and closes the file
with open('moby-dick.txt', 'r') as f:
    print(f.read().count("e"))

print("This is the end!")
# additional print txt - not part of task
