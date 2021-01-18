type(32)
max('Hello world') # also with numbers of course
min('Hello world')
len('Hello world')

int('32')
float(32)
int(3.99)
str(32)

import math

math.log10(10)
math.sin(180)

import random
x = random.random()
random.randint(0,100)
random.choice([1,2,3,5,9,10])


str = "Simple string"
for char in str:
    print(char)

dir(str) # lists all available methods in the string prototype


camels = 42
print("I have spotted %d camels." % camels)
print("I have spotted %d camels in %s." % (camels, "Sahara desert"))

# % modulo operator
# ** exponential operator
# / float division
# // integer division


a = 13
b = 13
a == b # True
a is b # True

c = [1,2,3]
d = [1,2,3]
c == d # True
c is d # False

clone = c
c is clone # True