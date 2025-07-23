#Task 1
#    Task 1
#    - Create a function that updates a dictionary (dct) with a new key-value pair.
#    - If the key already exists in dct, print the original value, then update its value.
#    - Return the updated dictionary.
#    """
#    return

def update_dictionary(dct, key, value):
    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")
    dct[key] = value
    return dct

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

updated1 = update_dictionary({}, "name", "Alice")
print(updated1)  # Output includes original value and updated dictionary

updated2 = update_dictionary({"age": 25}, "age", 26)
print(updated2)  # Output includes original value and updated dictionary
