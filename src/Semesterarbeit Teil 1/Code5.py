import time
import matplotlib.pyplot as plt

# THIS CLASS TAKES SEVERAL MINUTES TO RUN!!!
number_of_calls = 15001
# YOU CAN DECREASE THE NUMBER OF CALLS HERE IF YOU WANT


# Function with dynamic programming, instantiates an emtpy array and fills it with fibonacci-numbers
def fib_iterative_dynamic(n):
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


x_values = []
y_values_dynamic = []
y_values_append = []
y_values_replace = []


def code5():
    print(
        f"Measure and compare the time needed to calculate {number_of_calls-1} fibonacci-numbers with iterative "
        f"functions")

    for i in range(number_of_calls):
        x_values.append(i)
        time_total = 0
        fib_result = fib_iterative_dynamic(i)

        for j in range(30):
            start_time = time.perf_counter_ns()
            fib_result = fib_iterative_dynamic(i)
            end_time = time.perf_counter_ns()
            duration = end_time - start_time
            time_total += duration

        average_duration = time_total / 30
        print(f"DYNAMIC - {i}.te Fibonacci-Number: {fib_result}; Time needed: {round(average_duration)}")
        y_values_dynamic.append(average_duration)

        time_total = 0
        fib_result = fib_iterative_append(i)

        for j in range(30):
            start_time = time.perf_counter_ns()
            fib_result = fib_iterative_append(i)
            end_time = time.perf_counter_ns()
            duration = end_time - start_time
            time_total += duration

        average_duration = time_total / 30
        print(f"APPEND -  {i}.te Fibonacci-Number: {fib_result}; Time needed: {round(average_duration)}")
        y_values_append.append(average_duration)

        time_total = 0
        fib_result = fib_iterative_replace(i)

        for j in range(30):
            start_time = time.perf_counter_ns()
            fib_result = fib_iterative_replace(i)
            end_time = time.perf_counter_ns()
            duration = end_time - start_time
            time_total += duration

        average_duration = time_total / 30
        print(f"REPLACE - {i}.te Fibonacci-Number: {fib_result}; Time needed: {round(average_duration)}")
        y_values_replace.append(average_duration)

    plt.xlabel("n-th Fibonacci Number")
    plt.ylabel("Time needed in Nanoseconds")

    plt.plot(x_values, y_values_dynamic, label='Dynamic-Function', color='red')
    plt.plot(x_values, y_values_append, label='Append-Function', color='blue')
    plt.plot(x_values, y_values_replace, label='Replace-Function', color='green')
    plt.legend()
    plt.show()


code5()

