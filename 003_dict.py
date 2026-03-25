#DICT
# {}, keys, no duplicates allowed, ordered, mutable


my_dict = {
    "Name":"Rohan",
    "Age":35,
    "Gender":"Male",
    "Name" : "Sohan"
}

#access 'Rohan'
print(my_dict["Name"])

print(my_dict)

# update age to 25
my_dict["Age"] = 25
print(my_dict)

#########################################################################
# ITEMS     SYMBOL      ORDERED     CALLING     MUTABLE     DUPLICATES
# LIST        []           Y         Index        Y             Y
# DICT        {}           Y         Keys         Y             N
# TUPLE       ()           Y         Index        N             Y
# SETS        {}           N          -           N             N