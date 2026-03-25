# STRING SLICING

my_string = "This is Instru Students"

# access first element
print(my_string[0])

# access second element
print(my_string[1])

# access 'This'
print(my_string[0:4])

# access 'Ti'
print(my_string[0:4:2])

# access last element
print(my_string[-1])

# second last element
print(my_string[-2])

# string reverse
print(my_string[::-1])

# reverse 'Students'
print(my_string[:-9:-1])

# upper case/ lower case
print(my_string.upper())
print(my_string.lower())

# replace in string
print(my_string.replace('s', 'X'))