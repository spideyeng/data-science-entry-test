#Task 1
def swap(x, y):
    # Check if both x and y are numeric (int or float)
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        print(f"Either or both variables are not numeric")
        return -1
    # Swap values
    x, y = y, x
    print(f"Swapped values: x = {x}, y = {y}")
    return x, y # Optional: returning the swapped values as a tuple


#Task 2
# - "Apple", 10
# - 9, 17
swap("Apple", 10)
swap(-9, 17)
