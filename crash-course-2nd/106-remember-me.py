import json

filename = 'username.json'


def get_stored_username():
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def store_username(username):
    with open(filename, 'w') as f:
        json.dump(username, f)


def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input('What is your name? ')
        store_username(username)
        print(f"We'll remember when you come back {username}")

greet_user()



