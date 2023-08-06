# get mass from user and convert to integer
m = int(input("m: "))

c = 300_000_000

# function for square
def square(n):
    return n * n

# einstein formula E = m * c * c
E =  m * square(c)

print("E:",E)
