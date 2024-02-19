import matplotlib.pyplot as plt
import time


def instantiate_buffer(n):
    global buffer
    buffer = [-1] * n
    buffer[0] = 0
    buffer[1] = 1


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


number_of_calls = 20001
x_values = []
y_values = []
buffer = []


def test4():
    print(
        f"Measure the time needed to calculate the n-th fibonacci-number with buffered recursive function")

    instantiate_buffer(number_of_calls)

    for i in range(number_of_calls):

        start_time = time.perf_counter_ns()
        fib_result = buffered_fib(i)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time

        print(f"{i}.te Fibonacci-Number: {fib_result}; Time needed: {duration}")
        x_values.append(i)
        y_values.append(duration)

    plt.xlabel("n-th Fibonacci Number")
    plt.ylabel("Time needed in Nanoseconds")

    plt.plot(x_values, y_values, color='black')
    plt.show()


test4()
