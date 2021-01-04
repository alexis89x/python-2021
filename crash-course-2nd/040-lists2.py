magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title())

print('Finished')


# numerical loops

for value in range(1,5):
    print(value) # Leaves out 5!! It goes from 1 to 4
print('========')

for value in range(5):
    print(value) # Leaves out 5!! It goes from ZERO to 4
print('========')

my_list = list(range(2,11, 2)) # 3rd argument is the step
print(my_list)

# Math info
min(my_list)
max(my_list)
sum(my_list)

# List comprehensions
new_list = [value**2 for value in range(1,11)]

# Slicing
players = ['alex', 'lily', 'plain', 'thorn', 'rome', 'milan']
part = players[0:3] # zero index to 2
part = players[:4] # zero to 3
part = players[2:] # 2 to end
part = players[-3:] # last three to end

for player in players[-3:]:
    print(player)

copy_players = players[:] # it is basically like slice(0)
