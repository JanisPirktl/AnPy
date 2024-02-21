import time
import matplotlib.pyplot as plt
import decimal
import sys
import numpy as np


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
sys.setrecursionlimit(20500)


def code13():
    print(f"Measure and compare the time needed to calculate single fibonacci-numbers with with all "
          f"functions")


    for i in range(1000, 11000, 1000):
        x_values.append(i)
        instantiate_buffer_iterative(i)
        instantiate_buffer_recursive(i)
        sqrt_of_5 = set_precision(round(i/4))

        total_time = 0
        for j in range(100):
            start_time = time.perf_counter_ns()
            fib_result_iterative_replace = fib_iterative_replace(i)
            end_time = time.perf_counter_ns()
            duration = end_time - start_time
            total_time += duration

        average_time = total_time / 100
        print(f"ITERATIVE REPLACE -  {i}.te Fibonacci-Number: {fib_result_iterative_replace}; Time needed: {round(average_time)}")
        y_values_iterative_replace.append(average_time)

        start_time = time.perf_counter_ns()
        fib_result_iterative_buffered = fib_iterative_buffered(i)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        print(f"ITERATIVE BUFFERED - {i}.te Fibonacci-Number: {fib_result_iterative_buffered}; Time needed: {duration}")
        y_values_iterative_buffered.append(duration)

        start_time = time.perf_counter_ns()
        fib_result_recursive_buffered = buffered_fib(i)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        print(f"RECURSIVE BUFFERED - {i}.te Fibonacci-Number: {fib_result_recursive_buffered}; Time needed: {duration}")
        y_values_recursive_buffered.append(duration)

        start_time = time.perf_counter_ns()
        fib_result_binet = fib_binet_precision(i, sqrt_of_5)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time

        print(f"BINET ENHANCED -     {i}.te Fibonacci-Number: {fib_result_binet}; Time needed: {round(duration)}")
        y_values_binet.append(duration)

        if fib_result_binet != fib_result_recursive_buffered or fib_result_binet != fib_result_iterative_buffered:
            print(f"RESULTS DO NOT MATCH AT {i}-th NUMBER!")

    plt.xlabel("n-th Fibonacci Number")
    plt.ylabel("Time needed in Nanoseconds")

    bar_width = 0.2
    r1 = np.arange(len(y_values_iterative_replace))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]
    r4 = [x + bar_width for x in r3]

    x_labels = ['1000', '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']
    plt.xticks([r + bar_width for r in range(len(y_values_iterative_replace))], x_labels)

    plt.bar(r1, y_values_iterative_replace, label='Iterative-Replace', color='red', width=bar_width, edgecolor='grey')
    plt.bar(r2, y_values_iterative_buffered, label='Iterative-Buffered', color='green', width=bar_width, edgecolor='grey')
    plt.bar(r3, y_values_recursive_buffered, label='Recursive-Buffered', color='yellow', width=bar_width, edgecolor='grey')
    plt.bar(r4, y_values_binet, label='Binet', color='blue', width=bar_width, edgecolor='grey')

    plt.legend()
    plt.show()


code13()
