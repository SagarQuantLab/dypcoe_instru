# FOR LOOP
# for i in iterable_obj:
#       print(i)

# for i in range(6):
#     print(i)
# for i in range(0,6):
#     print(i)
for i in range(0,6,2):
    print(i)

my_list = [1, 3, 5, 2, 8, 8]
# access all index of list
for i in range(len(my_list)):
    print(i)

# access all elements of list
for i in my_list:
    print(i)

# access all elements along with index
i = 0
for each_element in my_list:
    print(each_element, i )
    i += 1

# access element from index
for i in range(len(my_list)):
    print(i, my_list[i])

# access index and value together
for i, val in enumerate(my_list):
    print(i, val)

###########
# for loop in dictionary

my_dict = {
    "Name": "Rohan",
    "Age": 35,
    "Gender": "Male"
}

# print keys
for i in my_dict.keys():
    print(i)

# access values
for i in my_dict.values():
    print(i)

# access all items
for i in my_dict.items():
    print(i)

# access value using index
for each_key in my_dict.keys():
    print(each_key, my_dict[each_key])