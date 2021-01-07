alien = { 'color': 'green', 'points': 5 }
print(alien['color'])

alien['test'] = True
print(alien)

empty_alien = {}

del alien['test']

points = alien.get('points', 'value in case it does not exist')
# if you omit the second value, it returns None


for key, value in alien.items():
    print(f"key: {key}")
    print(f"value: {value}")

# for key in alien.keys():
# for value in alien.values():
# for key in sorted(alien.keys()):
# for value in set(alien.values()): # this eliminates duplicate values

# this is a set
setName = { 'python', 'c', 'scala '}

alien0 = { 'color': 'green', 'points': 6 }
alien1 = { 'color': 'green', 'points': 7 }
alien2 = { 'color': 'green', 'points': 9 }
list_aliens = [ alien0, alien1, alien2 ]

for index in range(30):
    new_alien = { 'id': index, 'name': "Ciao" }
    list_aliens.append(new_alien)

