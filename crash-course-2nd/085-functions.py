def make_pizza(size, *toppings):
    # print(toppings)
    print(f'\nMaking a {size}-inch pizza with the following toppings:')

    for topping in toppings:
        print(f"\t- {topping}")

make_pizza(12, 'Pepperoni')
make_pizza(16, 'Luca', 'Toni')


def build_profile(first_name, last_name, **user_info):
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info

print(build_profile('Alessandro', 'Piana', age=31, height=181))

