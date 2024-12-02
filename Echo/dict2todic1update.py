# Sample dictionaries
dict1 = {
    'a': 1,
    'b': 2,
    'c': 3
}

dict2 = {
    'b': 20,
    'c': 30,
    'd': 40
}

# Update dict2 with values from dict1 where keys match
for key in dict1.keys() & dict2.keys():
    dict2[key] = dict1[key]

# Print updated dict2
print("Updated dict2:", dict2)
