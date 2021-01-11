with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

# Line by line
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print("\n - " + line.rstrip())

    # or lines = file_object.readlines()

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
    full = ""
    for line in lines:
        full += line.strip()
    print(full)