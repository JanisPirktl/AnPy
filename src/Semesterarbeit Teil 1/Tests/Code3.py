import matplotlib.pyplot as plt
import time


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


number_of_calls = 26
x_values = []
y_values = []


def test3():
    print(f"Measure the time needed to calculate the n-th fibonacci-number with recursive function")

    for i in range(number_of_calls):
        fib_result = fib(i)
        time_total = 0

        for j in range(100):
            start_time = time.perf_counter_ns()
            fib_result = fib(i)
            end_time = time.perf_counter_ns()
            duration = end_time - start_time
            time_total += duration

        average_duration = time_total / 100
        print(
            f"{i}.te Fibonacci-Number: {fib_result}; Time needed: {round(average_duration)}"
            f" nanoseconds")
        x_values.append(i)
        y_values.append(average_duration)

    plt.xlabel("n-th Fibonacci Number")
    plt.ylabel("Time needed in Nanoseconds")

    plt.plot(x_values, y_values, color='black')
    plt.show()


test3()
