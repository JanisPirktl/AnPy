import time
import math

# Number of Fibonacci numbers to calculate
number_of_calls = 1001

# Number of Fibonacci numbers to calculate with recursive
number_of_calls_for_recursive = 31


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


# Iterative function with replacing new numbers in the array
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


def test1():
    print(f"Calculate the {number_of_calls_for_recursive} first fibonacci-numbers with recursive function")
    for i in range(number_of_calls_for_recursive):
        counter = fib_calls(i, [0])[1][0]
        start_time = time.perf_counter_ns()
        fib_result = fib(i)
        end_time = time.perf_counter_ns()
        duration_recursive = end_time - start_time
        print(
            f"{i}.te Fibonacci-Number:          {fib_result};      Needed time: {duration_recursive} nanoseconds;         Number of calls: {counter}")


def test2():
    print("Calculate average time needed with binet's formula if the function is alone in the loop")
    print(
        "Calculate the 30 first fibonacci-numbers with recursive function in advance to guarantee that the variables needed for binet's formula are not in the data-registers or the caches of the cpu")

    for i in range(number_of_calls_for_recursive):
        fib_result = fib(i)

    total_binet_time = 0
    for i in range(number_of_calls_for_recursive):
        start_time = time.perf_counter_ns()
        fib_result = fib_binet(i)
        end_time = time.perf_counter_ns()
        duration_binet = end_time - start_time
        total_binet_time += duration_binet
        print(
            f"{i}.te Fibonacci-Number:         {fib_result};        Needed time: {duration_binet} nanoseconds;")
    average_binet_time = total_binet_time / number_of_calls_for_recursive
    print(f"binet needed average time of {round(average_binet_time)} nanoseconds (alone in the loop), no variables needed were in the registers or the caches in advance")


def test3():
    print("Calculate average time needed with binet's formula if the function is alone in the loop")
    print(
        "Calculate the 30 first fibonacci-numbers with the function that uses binet's formula in advance to check for a difference in the average time need if that the variables needed for binet's formula are already in the data-registers or the caches of the cpu")

    for i in range(number_of_calls_for_recursive):
        fib_result = fib_binet(i)

    total_binet_time = 0
    for i in range(number_of_calls_for_recursive):
        start_time = time.perf_counter_ns()
        fib_result = fib_binet(i)
        end_time = time.perf_counter_ns()
        duration_binet = end_time - start_time
        total_binet_time += duration_binet
        print(
            f"{i}.te Fibonacci-Number:         {fib_result};        Needed time: {duration_binet} nanoseconds;")
    average_binet_time = total_binet_time / number_of_calls_for_recursive
    print(f"binet needed average time of {round(average_binet_time)} nanoseconds (alone in the loop), the needed variables were in the registers or the caches in advance")


def test4():
    print("Calculate average time needed with binet's formula if the function is NOT alone in the loop")
    print(
        "Calculate the 30 first fibonacci-numbers with recursive function in advance to guarantee that the variables needed for binet's formula are not in the data-registers or the caches of the cpu")

    for i in range(number_of_calls_for_recursive):
        fib_result = fib(i)

    total_binet_time = 0
    for i in range(number_of_calls_for_recursive):
        fib_result = fib(number_of_calls_for_recursive)
        start_time = time.perf_counter_ns()
        fib_result = fib_binet(i)
        end_time = time.perf_counter_ns()
        duration_binet = end_time - start_time
        total_binet_time += duration_binet
        print(
            f"{i}.te Fibonacci-Number:         {fib_result};      Needed time: {duration_binet} nanoseconds;")
    average_binet_time = total_binet_time / number_of_calls_for_recursive
    print(f"binet needed average time of {round(average_binet_time)} nanoseconds (not alone in the loop), the needed variables were not in the registers or caches in advance")



# Compare the time needed for the dynamic function, the iterative function with replace and the iterative function with append in every possible order to check for differences
def test5():
    print("Find out which function is the fastest")
    iterative_was_faster = 0
    dynamic_was_faster = 0
    iterative_append_was_faster = 0
    for i in range(number_of_calls):
        print(f"{i}.te Fibonacci-Number:")

        start_time = time.perf_counter_ns()
        fib_result = fib_dynamic(i)
        end_time = time.perf_counter_ns()
        duration_dynamic = end_time - start_time
        print(
            f"Dynamic:                {fib_result};   Needed time: {duration_dynamic} Nanoseconds;")

        start_time = time.perf_counter_ns()
        fib_result = fib_iterative_replace(i)
        end_time = time.perf_counter_ns()
        duration_iterative_replace = end_time - start_time
        print(
            f"Iterative:              {fib_result};   Needed time: {duration_iterative_replace} Nanoseconds;")

        start_time = time.perf_counter_ns()
        fib_result = fib_iterative_append(i)
        end_time = time.perf_counter_ns()
        duration_iterative_append = end_time - start_time
        print(
            f"Iterative_append:       {fib_result};   Needed time: {duration_iterative_append} Nanoseconds;")

        print()
        if duration_dynamic < duration_iterative_replace and duration_dynamic < duration_iterative_append:
            dynamic_was_faster += 1
        if duration_iterative_replace < duration_dynamic and duration_iterative_replace < duration_iterative_append:
            iterative_was_faster += 1
        if duration_iterative_append < duration_iterative_replace and duration_iterative_append < duration_dynamic:
            iterative_append_was_faster += 1

    print(f"Iterative was faster {iterative_was_faster} times")
    print(f"Dynamic was faster {dynamic_was_faster} times")
    print(f"Iterative_append was faster {iterative_append_was_faster} times")


def test6():
    print("Find out which function is the fastest")
    iterative_was_faster = 0
    dynamic_was_faster = 0
    iterative_append_was_faster = 0
    for i in range(number_of_calls):
        print(f"{i}.te Fibonacci-Number:")

        start_time = time.perf_counter_ns()
        fib_result = fib_dynamic(i)
        end_time = time.perf_counter_ns()
        duration_dynamic = end_time - start_time
        print(
            f"Dynamic:                {fib_result};   Needed time: {duration_dynamic} Nanoseconds;")

        start_time = time.perf_counter_ns()
        fib_result = fib_iterative_append(i)
        end_time = time.perf_counter_ns()
        duration_iterative_append = end_time - start_time
        print(
            f"Iterative_append:       {fib_result};   Needed time: {duration_iterative_append} Nanoseconds;")

        start_time = time.perf_counter_ns()
        fib_result = fib_iterative_replace(i)
        end_time = time.perf_counter_ns()
        duration_iterative_replace = end_time - start_time
        print(
            f"Iterative:              {fib_result};   Needed time: {duration_iterative_replace} Nanoseconds;")

        print()
        if duration_dynamic < duration_iterative_replace and duration_dynamic < duration_iterative_append:
            dynamic_was_faster += 1
        if duration_iterative_replace < duration_dynamic and duration_iterative_replace < duration_iterative_append:
            iterative_was_faster += 1
        if duration_iterative_append < duration_iterative_replace and duration_iterative_append < duration_dynamic:
            iterative_append_was_faster += 1

    print(f"Iterative was faster {iterative_was_faster} times")
    print(f"Dynamic was faster {dynamic_was_faster} times")
    print(f"Iterative_append was faster {iterative_append_was_faster} times")


def test7():
    print("Find out which function is the fastest")
    iterative_was_faster = 0
    dynamic_was_faster = 0
    iterative_append_was_faster = 0
    for i in range(number_of_calls):
        print(f"{i}.te Fibonacci-Number:")

        start_time = time.perf_counter_ns()
        fib_result = fib_iterative_replace(i)
        end_time = time.perf_counter_ns()
        duration_iterative_replace = end_time - start_time
        print(
            f"Iterative:              {fib_result};   Needed time: {duration_iterative_replace} Nanoseconds;")

        start_time = time.perf_counter_ns()
        fib_result = fib_dynamic(i)
        end_time = time.perf_counter_ns()
        duration_dynamic = end_time - start_time
        print(
            f"Dynamic:                {fib_result};   Needed time: {duration_dynamic} Nanoseconds;")

        start_time = time.perf_counter_ns()
        fib_result = fib_iterative_append(i)
        end_time = time.perf_counter_ns()
        duration_iterative_append = end_time - start_time
        print(
            f"Iterative_append:       {fib_result};   Needed time: {duration_iterative_append} Nanoseconds;")

        print()
        if duration_dynamic < duration_iterative_replace and duration_dynamic < duration_iterative_append:
            dynamic_was_faster += 1
        if duration_iterative_replace < duration_dynamic and duration_iterative_replace < duration_iterative_append:
            iterative_was_faster += 1
        if duration_iterative_append < duration_iterative_replace and duration_iterative_append < duration_dynamic:
            iterative_append_was_faster += 1

    print(f"Iterative was faster {iterative_was_faster} times")
    print(f"Dynamic was faster {dynamic_was_faster} times")
    print(f"Iterative_append was faster {iterative_append_was_faster} times")


def test8():
    print("Find out which function is the fastest")
    iterative_was_faster = 0
    dynamic_was_faster = 0
    iterative_append_was_faster = 0
    for i in range(number_of_calls):
        print(f"{i}.te Fibonacci-Number:")

        start_time = time.perf_counter_ns()
        fib_result = fib_iterative_replace(i)
        end_time = time.perf_counter_ns()
        duration_iterative_replace = end_time - start_time
        print(
            f"Iterative:              {fib_result};   Needed time: {duration_iterative_replace} Nanoseconds;")

        start_time = time.perf_counter_ns()
        fib_result = fib_iterative_append(i)
        end_time = time.perf_counter_ns()
        duration_iterative_append = end_time - start_time
        print(
            f"Iterative_append:       {fib_result};   Needed time: {duration_iterative_append} Nanoseconds;")

        start_time = time.perf_counter_ns()
        fib_result = fib_dynamic(i)
        end_time = time.perf_counter_ns()
        duration_dynamic = end_time - start_time
        print(
            f"Dynamic:                {fib_result};   Needed time: {duration_dynamic} Nanoseconds;")

        print()
        if duration_dynamic < duration_iterative_replace and duration_dynamic < duration_iterative_append:
            dynamic_was_faster += 1
        if duration_iterative_replace < duration_dynamic and duration_iterative_replace < duration_iterative_append:
            iterative_was_faster += 1
        if duration_iterative_append < duration_iterative_replace and duration_iterative_append < duration_dynamic:
            iterative_append_was_faster += 1

    print(f"Iterative was faster {iterative_was_faster} times")
    print(f"Dynamic was faster {dynamic_was_faster} times")
    print(f"Iterative_append was faster {iterative_append_was_faster} times")


def test9():
    print("Find out which function is the fastest")
    iterative_was_faster = 0
    dynamic_was_faster = 0
    iterative_append_was_faster = 0
    for i in range(number_of_calls):
        print(f"{i}.te Fibonacci-Number:")

        start_time = time.perf_counter_ns()
        fib_result = fib_iterative_append(i)
        end_time = time.perf_counter_ns()
        duration_iterative_append = end_time - start_time
        print(
            f"Iterative_append:       {fib_result};   Needed time: {duration_iterative_append} Nanoseconds;")

        start_time = time.perf_counter_ns()
        fib_result = fib_dynamic(i)
        end_time = time.perf_counter_ns()
        duration_dynamic = end_time - start_time
        print(
            f"Dynamic:                {fib_result};   Needed time: {duration_dynamic} Nanoseconds;")

        start_time = time.perf_counter_ns()
        fib_result = fib_iterative_replace(i)
        end_time = time.perf_counter_ns()
        duration_iterative_replace = end_time - start_time
        print(
            f"Iterative:              {fib_result};   Needed time: {duration_iterative_replace} Nanoseconds;")

        print()
        if duration_dynamic < duration_iterative_replace and duration_dynamic < duration_iterative_append:
            dynamic_was_faster += 1
        if duration_iterative_replace < duration_dynamic and duration_iterative_replace < duration_iterative_append:
            iterative_was_faster += 1
        if duration_iterative_append < duration_iterative_replace and duration_iterative_append < duration_dynamic:
            iterative_append_was_faster += 1

    print(f"Iterative was faster {iterative_was_faster} times")
    print(f"Dynamic was faster {dynamic_was_faster} times")
    print(f"Iterative_append was faster {iterative_append_was_faster} times")


def test10():
    print("Find out which function is the fastest")
    iterative_was_faster = 0
    dynamic_was_faster = 0
    iterative_append_was_faster = 0
    for i in range(number_of_calls):
        print(f"{i}.te Fibonacci-Number:")

        start_time = time.perf_counter_ns()
        fib_result = fib_iterative_append(i)
        end_time = time.perf_counter_ns()
        duration_iterative_append = end_time - start_time
        print(
            f"Iterative_append:       {fib_result};   Needed time: {duration_iterative_append} Nanoseconds;")

        start_time = time.perf_counter_ns()
        fib_result = fib_iterative_replace(i)
        end_time = time.perf_counter_ns()
        duration_iterative_replace = end_time - start_time
        print(
            f"Iterative:              {fib_result};   Needed time: {duration_iterative_replace} Nanoseconds;")

        start_time = time.perf_counter_ns()
        fib_result = fib_dynamic(i)
        end_time = time.perf_counter_ns()
        duration_dynamic = end_time - start_time
        print(
            f"Dynamic:                {fib_result};   Needed time: {duration_dynamic} Nanoseconds;")

        print()
        if duration_dynamic < duration_iterative_replace and duration_dynamic < duration_iterative_append:
            dynamic_was_faster += 1
        if duration_iterative_replace < duration_dynamic and duration_iterative_replace < duration_iterative_append:
            iterative_was_faster += 1
        if duration_iterative_append < duration_iterative_replace and duration_iterative_append < duration_dynamic:
            iterative_append_was_faster += 1

    print(f"Iterative was faster {iterative_was_faster} times")
    print(f"Dynamic was faster {dynamic_was_faster} times")
    print(f"Iterative_append was faster {iterative_append_was_faster} times")

print("Test 1")
test1()
print()
print("Test 2")
test2()
print()
print("Test 3")
test3()
print()
print("Test 4")
test4()
print()
print("Test 5")
test5()
print()
print("Test 6")
test6()
print()
print("Test 7")
test7()
print()
print("Test 8")
test8()
print()
print("Test 9")
test9()
print()
print("Test 10")
test10()