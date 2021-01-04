cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Comparisons: ==, !=, >, <, >=, <=, and, or
if 'audi' in cars:
    print('Audi is available')

if 'fiat' not in cars:
    print('I need a Panda')

age = 25

if age < 10:
    print('Too low')
elif age < 20:
    print('Still low')
else:
    print('Ok')

# checj for empty list
list2 = []
if list2:
    print('there are value')
else:
    print('there are not')

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}')
    else:
        print(f'Topping {requested_topping} is not available')

print('Finished making this pizzaaaaa')