def greet_user():
    print('Hello')


greet_user()


def greet_user_name(name):
    print(f'Hello, {name}')


greet_user_name('Alex')


def describe_pet(pet_name, pet_type = 'dog'):
    print(f'You {pet_type} is called {pet_name}')


describe_pet('Nanuk', 'dog')

describe_pet(pet_type='cat', pet_name='Yuki')


def get_formatted_name(first_name, last_name):
    return f"{first_name} {last_name}".title()

print(get_formatted_name('alex', 'plain'))


def change_list(names):
    while names:
        print(names.pop())

my_names = ['a', 'b', 'c']
change_list(my_names[:]) # like JS slices...