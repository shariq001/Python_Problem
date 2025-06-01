# Problem 3: Sum of Digits
# Write a function that takes a non-negative integer and returns the sum of its digits.

def sum_digits( number ):
    
    return sum(int(digit) for digit in str(number))

print(sum_digits(12538))