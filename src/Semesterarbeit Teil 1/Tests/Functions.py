import math
import decimal

# Global Buffer List used in buffered_fib()
buffer = []


# Recursive Function
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# Function to count the function calls of the recursive function
def fib_calls(n, counter):
    counter[0] += 1
    if n <= 1:
        return n, counter
    else:
        n_1, counter = fib_calls(n-1, counter)
        n_2, counter = fib_calls(n-2, counter)
        return n_1 + n_2, counter


# Instantiate a "Buffer" list to avoid doing redundant calculations
def instantiate_buffer(n):
    global buffer
    buffer = [-1] * (n + 1)
    buffer[0] = 0
    buffer[1] = 1


# Uses a "Buffer" List to minimize function calls
def buffered_fib(n):
    global buffer
    if buffer[n] != -1:
        return buffer[n]
    if buffer[n - 1] != -1:
        n_1 = buffer[n - 1]
    else:
        n_1 = buffered_fib(n - 1)
        buffer[n - 1] = n_1
    if buffer[n - 2] != -1:
        n_2 = buffer[n - 2]
    else:
        n_2 = buffered_fib(n - 2)
        buffer[n - 2] = n_2
    return n_1 + n_2




# Function with dynamic programming, instantiates an emtpy array and fills it with fibonacci-numbers
def fib_dynamic(n):
    if n <= 1:
        return n
    fib_numbers = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib_numbers[i] = fib_numbers[i - 1] + fib_numbers[i - 2]
    return fib_numbers[n]


# Iterative function with replacing, uses an array with just 2 numbers
def fib_iterative_replace(n):
    if n <= 1:
        return n
    fib_numbers = [0, 1]
    for i in range(1, n):
        current = fib_numbers[0]
        fib_numbers[0] = fib_numbers[1]
        fib_numbers[1] = current + fib_numbers[0]
    return fib_numbers[1]


# Iterative function with appending new numbers to the array
def fib_iterative_append(n):
    if n <= 1:
        return n
    fib_numbers = [0, 1]
    for i in range(1, n):
        fib_numbers.append((fib_numbers[-1] + fib_numbers[-2]))
    return fib_numbers[-1]


# Function with Binet's formula
def fib_binet(n):
    golden_ratio = (1 + math.sqrt(5)) / 2
    return round((golden_ratio ** n - (1 - golden_ratio) ** n) / math.sqrt(5))


# Calculates desired decimal places of square root of 5
def set_precision(precision):
    decimal.getcontext().prec = precision
    five = decimal.Decimal(5)
    return five.sqrt()

# Enhanced Function with Binet's formula, able to calculate higher fibonacci-numbers
def fib_binet_precision(n, sqrt_of_5):
    golden_ratio = (1 + sqrt_of_5) / 2
    return round((golden_ratio ** n - (1 - golden_ratio) ** n) / sqrt_of_5)