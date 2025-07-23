#Task 1
#- Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
#    - lst must be a list.
#   - Return the modified list.
#    """
#    return

def find_and_replace(lst, find_val, replace_val):
    return [replace_val if item == find_val else item for item in lst]

#Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

#First List
list_uno = [1, 2, 3, 4, 2, 2]
print(f"Original List Uno: {list_uno}")
updated_list_uno = find_and_replace(list_uno,2,5)
print(f"Updated List Uno: {updated_list_uno}")

#Second List
list_dos = ["apple", "banana", "apple"]
print(f"Original List Dos: {list_dos}")
updated_list_dos = find_and_replace(list_dos,"apple","orange")
print(f"Updated List Dos: {updated_list_dos}")



