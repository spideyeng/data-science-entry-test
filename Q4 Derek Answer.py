#Task 1
#    - Create a function that reverses a given string (s).
#    - s must be a string.
#    - Return the reversed string.
#    """
#    return

def string_reverse(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    return s[::-1]

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

text1 = "Hello World"
reversed_text1 = string_reverse(text1)
print(f"Original Text1: {text1}")
print(f"Reversed Text1: {reversed_text1}")

text2 = "Python"
reversed_text2 = string_reverse(text2)
print(f"Original Text2: {text2}")
print(f"Reversed Text2: {reversed_text2}")

text3 = 123456
reversed_text3 = string_reverse(text3)
print(f"Original Text3: {text3}")
print(f"Reversed Text3: {reversed_text3}")