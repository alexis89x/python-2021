import json

numbers = [2,3,5,7,11,13]
filename = 'numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f)


# load json
with open(filename) as f:
    numbers2 = json.load(f)

print(numbers2)

username = 'Eric'
filename2 = 'username.json'
with open(filename2, 'w') as f2:
    json.dump(username, f2)