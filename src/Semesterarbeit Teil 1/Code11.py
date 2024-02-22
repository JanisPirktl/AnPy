import time
import matplotlib.pyplot as plt
import decimal


def fib_iterative_replace(n):
    if n <= 1:
        return n
    fib_numbers = [0, 1]
    for i in range(1, n):
        current = fib_numbers[0]
        fib_numbers[0] = fib_numbers[1]
        fib_numbers[1] = current + fib_numbers[0]
    return fib_numbers[1]


def instantiate_buffer_recursive(n):
    global buffer_recursive
    buffer_recursive = [-1] * (n + 1)
    buffer_recursive[0] = 0
    buffer_recursive[1] = 1


def buffered_fib(n):
    global buffer_recursive
    if buffer_recursive[n] != -1:
        return buffer_recursive[n]
    if buffer_recursive[n - 1] != -1:
        n_1 = buffer_recursive[n - 1]
    else:
        n_1 = buffered_fib(n - 1)
        buffer_recursive[n - 1] = n_1
    if buffer_recursive[n - 2] != -1:
        n_2 = buffer_recursive[n - 2]
    else:
        n_2 = buffered_fib(n - 2)
        buffer_recursive[n - 2] = n_2
    return n_1 + n_2


def instantiate_buffer_iterative(n):
    global buffer_iterative
    buffer_iterative = [-1] * (n + 1)
    buffer_iterative[0] = 0
    buffer_iterative[1] = 1


def fib_iterative_buffered(n):
    global buffer_iterative
    if n <= 1:
        return n
    if buffer_iterative[n] != -1:
        return buffer_iterative[n]
    if buffer_iterative[n - 1] != -1 and buffer_iterative[n - 2] != -1:
        buffer_iterative[n] = buffer_iterative[n - 1] + buffer_iterative[n - 2]
        return buffer_iterative[n]
    for i in range(2, n + 1):
        buffer_iterative[i] = buffer_iterative[i - 1] + buffer_iterative[i - 2]
    return buffer_iterative[n]


def set_precision(precision):
    decimal.getcontext().prec = precision
    five = decimal.Decimal(5)
    return five.sqrt()


def fib_binet_precision(n, sqrt_of_5):
    golden_ratio = (1 + sqrt_of_5) / 2
    return round((golden_ratio ** n - (1 - golden_ratio) ** n) / sqrt_of_5)


buffer_recursive = []
buffer_iterative = []
x_values = []
y_values_binet = []
y_values_iterative_buffered = []
y_values_recursive_buffered = []
y_values_iterative_replace = []
number_of_calls = 1001


def code11():
    print(f"Measure and compare the time needed to calculate {number_of_calls-1} fibonacci-numbers with with all "
          f"functions")
    instantiate_buffer_iterative(number_of_calls)
    instantiate_buffer_recursive(number_of_calls)


    for i in range(75, number_of_calls):
        x_values.append(i)
        start_time = time.perf_counter_ns()
        fib_result = fib_iterative_buffered(i)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        print(f"ITERATIVE BUFFERED - {i}.te Fibonacci-Number: {fib_result}; Time needed: {duration}")
        y_values_iterative_buffered.append(duration)

    for i in range(75, number_of_calls):
        start_time = time.perf_counter_ns()
        fib_result = buffered_fib(i)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        print(f"RECURSIVE BUFFERED - {i}.te Fibonacci-Number: {fib_result}; Time needed: {duration}")
        y_values_recursive_buffered.append(duration)

    for i in range(75, number_of_calls):
        sqrt_of_5 = set_precision(round(i/4))
        start_time = time.perf_counter_ns()
        fib_result = fib_binet_precision(i, sqrt_of_5)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        print(f"BINET ENHANCED -     {i}.te Fibonacci-Number: {fib_result}; Time needed: {duration}")
        y_values_binet.append(duration)

    for i in range(75, number_of_calls):
        total_time = 0
        for j in range(100):
            start_time = time.perf_counter_ns()
            fib_result = fib_iterative_replace(i)
            end_time = time.perf_counter_ns()
            duration = end_time - start_time
            total_time += duration

        average_time = total_time / 100
        print(f"ITERATIVE REPLACE -  {i}.te Fibonacci-Number: {fib_result}; Time needed: {round(average_time)}")
        y_values_iterative_replace.append(average_time)


    plt.xlabel("n-th Fibonacci Number")
    plt.ylabel("Time needed in Nanoseconds")

    plt.plot(x_values, y_values_iterative_replace, label='Iterative-Replace', color='red')
    plt.plot(x_values, y_values_iterative_buffered, label='Iterative-Buffered', color='green')
    plt.plot(x_values, y_values_recursive_buffered, label='Recursive-Buffered', color='orange')
    plt.plot(x_values, y_values_binet, label='Binet', color='blue')

    plt.legend()
    plt.show()


code11()
