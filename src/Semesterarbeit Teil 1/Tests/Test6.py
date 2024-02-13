import Functions as F
import time
import matplotlib.pyplot as plt

number_of_calls = 10001
x_values = []
y_values_dynamic = []
y_values_append = []
y_values_replace = []


def test6():
    print(
        f"Measure and compare the time needed to calculate {number_of_calls-1}-th fibonacci-numbers with iterative functions")

    for i in range(number_of_calls):

        x_values.append(i)

        start_time = time.perf_counter_ns()
        fib_result = F.fib_iterative_dynamic(i)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        print(f"DYNAMIC - {i}.te Fibonacci-Number: {fib_result}; Time needed: {duration}")
        y_values_dynamic.append(duration)

        start_time = time.perf_counter_ns()
        fib_result = F.fib_iterative_append(i)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        print(f"APPEND - {i}.te Fibonacci-Number: {fib_result}; Time needed: {duration}")
        y_values_append.append(duration)

        start_time = time.perf_counter_ns()
        fib_result = F.fib_iterative_replace(i)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        print(f"REPLACE - {i}.te Fibonacci-Number: {fib_result}; Time needed: {duration}")
        y_values_replace.append(duration)

    plt.xlabel("n-th Fibonacci Number")
    plt.ylabel("Time needed in Nanoseconds")

    plt.plot(x_values, y_values_dynamic, label='Dynamic-Function', color='red')
    plt.plot(x_values, y_values_append, label='Append-Function', color='blue')
    plt.plot(x_values, y_values_replace, label='Replace-Function', color='green')
    plt.legend()
    plt.show()


test6()

