message = input('tell me something: ')
print(message)

age = input('Tell me your age: ')
try:
    age = int(age)
except:
    print('Not a valid age')
    age = 0

if age >= 18:
    print('You are old enough')
else:
    print('You are too young to vote')

# Loops

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


while True:
    city = input('tell me a city, or "quit" to exit')
    if city == 'quit':
        break
    print(city)

# you can also use "continue" as in JS

list1 = ['a','b','c']
current_item = 0

while list1:
    current_item = list1.pop()


pets = ['cat', 'dog', 'cat', 'cat']
while 'cat' in pets:
    pets.remove('cat')

print(pets)