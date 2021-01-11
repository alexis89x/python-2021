filename = "programming.txt"
try:
    with open(filename, 'w') as file_object: # "a" for appending
        file_object.write('I love Python\n')
        file_object.write('I love Python 2')
except ZeroDivisionError:
    print("this exception should never happen")
except FileNotFoundError:
    print("File does not exist")
else:
    print("No exception!!")



def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist")
    except FileExistsError:
        pass #to fail silently
    else:
        words = contents.split()
        print(f"The file {filename} has {len(words)} words")

filenames = ['pizza.py', 'programming.txt', 'pi_digits.txt', 'impossible.txt']
for filename in filenames:
    count_words(filename)