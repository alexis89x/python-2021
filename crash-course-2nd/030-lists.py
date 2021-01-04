bicycles = ['a', 'b', 'c']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

# Work with lists
bicycles[0] = 'Wilier'
bicycles.append('Trek')
bicycles.insert(1, 'Cannondale')
del(bicycles[2])
print(bicycles)
popped_bicycle = bicycles.pop()
print(bicycles)
print(popped_bicycle)
# you can remove by value
bicycles.remove('c')
print(bicycles)

bicycles.sort()
bicycles.sort(reverse=True) # Notice that this is not a PURE function, the order will be changed!
# a PURE version would by
sorted_bicycles = sorted(bicycles, reverse=True)

bicycles.reverse()
len(bicycles)

# you can access last item in a list
bicycles[-1] # doesnt work only if list is empty
