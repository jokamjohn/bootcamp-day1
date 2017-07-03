"""
Function to generate a list of prime numbers from 0 to n.
"""


def prime_number(value):
    # Check if argument is an integer
    if isinstance(value, int):
        # Check if argument is positive integer
        if value > 0:
            values_set = set(range(2, value))
            prime_numbers = []
            # loop through while values_set is not empty
            while values_set:
                number = values_set.pop()
                prime_numbers.append(number)
                values_set.difference_update(set(range(number * 2, value + 1, number)))
            return prime_numbers
        else:
            # return empty list for a negative integer argument
            return []
    else:
        # raise a value error if argument is not an integer
        raise ValueError("Argument must be an integer")
