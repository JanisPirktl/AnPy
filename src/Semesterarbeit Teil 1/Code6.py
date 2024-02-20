import time
import matplotlib.pyplot as plt

# THIS CLASS TAKES SEVERAL MINUTES TO RUN!!!
number_of_calls = 10001
# YOU CAN DECREASE THE NUMBER OF CALLS HERE IF YOU WANT


def fib_iterative_replace(n):
    if n <= 1:
        return n
    fib_numbers = [0, 1]
    for i in range(1, n):
        current = fib_numbers[0]
        fib_numbers[0] = fib_numbers[1]
        fib_numbers[1] = current + fib_numbers[0]
    return fib_numbers[1]


def instantiate_buffer(n):
    global buffer
    buffer = [-1] * (n + 1)
    buffer[0] = 0
    buffer[1] = 1


def fib_iterative_buffered(n):
    global buffer
    if n <= 1:
        return n
    if buffer[n] != -1:
        return buffer[n]
    if buffer[n - 1] != -1 and buffer[n - 2] != -1:
        buffer[n] = buffer[n - 1] + buffer[n - 2]
        return buffer[n]
    for i in range(2, n + 1):
        buffer[i] = buffer[i - 1] + buffer[i - 2]
    return buffer[n]


buffer = []
x_values = []
y_values_replace = []
y_values_buffered = []


def code6():
    print(
        f"Measure and compare the time needed to calculate {number_of_calls-1} fibonacci-numbers with buffered and "
        f"non-buffered iterative functions")
    instantiate_buffer(number_of_calls)

    for i in range(number_of_calls):
        fib_result = fib_iterative_replace(i)
        x_values.append(i)
        time_total = 0

        for j in range(100):
            start_time = time.perf_counter_ns()
            fib_result = fib_iterative_replace(i)
            end_time = time.perf_counter_ns()
            duration = end_time - start_time
            time_total += duration

        average_duration = time_total / 100
        print(f"REPLACE - {i}.te Fibonacci-Number: {fib_result}; Time needed: {round(average_duration)}")
        y_values_replace.append(average_duration)

        start_time = time.perf_counter_ns()
        fib_result = fib_iterative_buffered(i)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        print(f"BUFFERED - {i}.te Fibonacci-Number: {fib_result}; Time needed: {duration}")
        y_values_buffered.append(duration)

    plt.xlabel("n-th Fibonacci Number")
    plt.ylabel("Time needed in Nanoseconds")

    plt.plot(x_values, y_values_buffered, label='Buffered-Function', color='red')
    plt.plot(x_values, y_values_replace, label='Replace-Function', color='green')

    plt.legend()
    plt.show()


code6()
