# Search for lines that contain 'From'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

# Search for lines that start with 'From'
if re.search('^From:', line):

# Search for lines that start with 'F', followed by # 2 characters, followed by 'm:'
if re.search('^F..m:', line):

# Search for lines that start with From and have an at sign
if re.search('^From:.+@', line):
    import re

# The findall() method searches the string in the second argument and returns a list of all of the strings that look like email addresses.
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)

# for all emails [a-zA-Z0-9]\S*@\S*[a-zA-Z]
# Search for lines that have an at sign between characters # The characters must be a letter or number
import re
hand = open('mbox-short.txt')
for line in hand:
line = line.rstrip()
x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line) if len(x) > 0:
print(x)

# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.
import re
hand = open('mbox-short.txt') for line in hand:
line = line.rstrip()
if re.search('^X\S*: [0-9.]+', line):
print(line)
# Code: http://www.py4e.com/code3/re10.py
# But now we have to solve the problem of extracting the numbers.


# Search for lines that start with 'X' followed by any # non whitespace characters and ':' followed by a space # and any number. The number can include a decimal.
# Then print the number if it is greater than zero. import re
hand = open('mbox-short.txt')
for line in hand:
line = line.rstrip()
x = re.findall('^X\S*: ([0-9.]+)', line) if len(x) > 0:
print(x)
# Code: http://www.py4e.com/code3/re11.py


# Search for lines that start with From and a character
# followed by a two digit number between 00 and 99 followed by ':' # Then print the number if it is greater than zero
import re
hand = open('mbox-short.txt')
for line in hand:
line = line.rstrip()
x = re.findall('^From .* ([0-9][0-9]):', line) if len(x) > 0: print(x)

# Escape Char
import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)