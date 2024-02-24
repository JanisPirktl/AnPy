import math
import time
import matplotlib.pyplot as plt


def fib_binet(n):
    golden_ratio = (1 + math.sqrt(5)) / 2
    return round((golden_ratio ** n - (1 - golden_ratio) ** n) / math.sqrt(5))


x_values = []
y_values_binet = []
y_values_iterative = []


def code10():
    print(f"Show that the average time needed for binet's function is misleading")
    time_total = 0

    for i in range(30):
        x_values.append(i)
        start_time = time.perf_counter_ns()
        fib_result = fib_binet(100)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        time_total += duration
        y_values_binet.append(duration)
        print(f"BINET - {100}.te Fibonacci-Number: {fib_result}; Time needed: {duration}")

    average_duration = time_total / 30
    y_values_average_binet = [average_duration] * 30

    plt.xlabel("Number of repetitions")
    plt.ylabel("Time needed in Nanoseconds")

    plt.plot(x_values, y_values_binet, label='Binet-Function', color='red')
    plt.plot(x_values, y_values_average_binet, label='Average-Binet', color='orange')

    plt.legend()
    plt.show()


code10()
