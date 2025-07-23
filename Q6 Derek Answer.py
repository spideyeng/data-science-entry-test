#    Task 1
#    - Create a function that finds the first negative number in a list (lst).
#    - Return the first negative number if found, otherwise return "No negatives".
#    - Use a while loop to implement this.
#    """
#    return

def find_first_negative(lst):
    i = 0
    while i < len(lst):
        if isinstance(lst[i], (int, float)) and lst[i] < 0:
            return lst[i]
        i += 1
    return "There are no negative numbers."

# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

numberlist1 = [3, 5, -1, 7, -2, 8]
print(f"1st Number List: {numberlist1}")
result1 = find_first_negative(numberlist1)
print(f"First negative number from 1st Number List: {result1}")

numberlist2 = [2,10,7,8]
print(f"Second Number List: {numberlist2}")
result2 = find_first_negative(numberlist2)
print(f"First negative number from 2nd Number List: {result2}")