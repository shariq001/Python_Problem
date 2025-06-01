# Problem 1: Reverse a String
# Write a function that takes a string as input and returns the reversed string.

def reverse_string( user_input ):
    print(user_input[::-1])

reverse_string("Hello")
reverse_string("Nothing Else")

# Now for s[::-1]:

# start is empty → means start from the end.

# stop is empty → go all the way to the beginning.

# step = -1 → move backwards (reverse direction).

# So, s[::-1] means:
# Start from the end of the string and go backwards one character at a time.