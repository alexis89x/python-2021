# A tuple is a list that cannot change
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 250 # causes an error

for dimension in dimensions:
    print(dimension)