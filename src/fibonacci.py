import time
import math

# Number of Fibonacci numbers to calculate
number_of_calls = 31


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
        return fib_calls(n - 1, counter) + fib_calls(n - 2, counter)


# Function with dynamic programming
def fib_dynamic(n):
    if n <= 1:
        return n
    fib_numbers = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib_numbers[i] = fib_numbers[i - 1] + fib_numbers[i - 2]
    return fib_numbers[n]


# Iterative function
def fib_iterative(n):
    if n <= 1:
        return n
    fib_numbers = [0, 1]
    for i in range(1, n):
        current = fib_numbers[0]
        fib_numbers[0] = fib_numbers[1]
        fib_numbers[1] = current + fib_numbers[0]
    return fib_numbers[1]


# Function with Binet's formula
def fib_binet(n):
    golden_ratio = (1 + math.sqrt(5)) / 2
    return round((golden_ratio ** n - (1 - golden_ratio) ** n) / math.sqrt(5))


for i in range(number_of_calls):
    if i < 31:
        print(f"{i}.te Fibonacci-Number:")
        counter = fib_calls(i, [0])[1][0]
        start_time = time.perf_counter_ns()
        fib_result = fib(i)
        end_time = time.perf_counter_ns()
        duration_recursive = end_time - start_time
        print(
            f"Recursive:    {fib_result};   Needed time: {duration_recursive} Nanoseconds;  Number of calls: {counter}")


iterative_was_faster = 0
dynamic_was_faster = 0
for i in range(number_of_calls):
    print(f"{i}.te Fibonacci-Number:")

    start_time = time.perf_counter_ns()
    fib_result = fib_dynamic(i)
    end_time = time.perf_counter_ns()
    duration_dynamic = end_time - start_time
    print(
        f"Dynamic:      {fib_result};   Needed time: {duration_dynamic} Nanoseconds;")

    start_time = time.perf_counter_ns()
    fib_result = fib_iterative(i)
    end_time = time.perf_counter_ns()
    duration_iterative = end_time - start_time
    print(
        f"Iterative:    {fib_result};   Needed time: {duration_iterative} Nanoseconds;")

    start_time = time.perf_counter_ns()
    fib_result = fib_binet(i)
    end_time = time.perf_counter_ns()
    duration_binet = end_time - start_time
    print(
        f"With Binet:   {fib_result};   Needed time: {duration_binet} Nanoseconds;")

    print()
    if duration_dynamic < duration_iterative:
        dynamic_was_faster += 1
    if duration_iterative < duration_dynamic:
        iterative_was_faster += 1

print(f"Iterative was faster {iterative_was_faster} times")
print(f"Dynamic was faster {dynamic_was_faster} times")
