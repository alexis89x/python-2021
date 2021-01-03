name = "alex plain"
print(name.title())
# upper(), lower()


first_name = "alex"
last_name = "plain"
full_name = f"{first_name.title()} {last_name.upper()}"
print(full_name)

# prior to python 3.6,
# full_name = "{} {}".format(first_name, last_name)

string_with_spaces = '   ciao    '
string_with_spaces.rstrip()
string_with_spaces.strip()
string_with_spaces.lstrip()

person = "Enzo Tortora"
quote = "Dove eravamo rimasti?"
all = f"{person} once said: '{quote}'"
print(all)


x, y, z = 1,2,3
MAX_CONNECTION = 4000 # constant-like although constants are not available in python

# >>> import this

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

