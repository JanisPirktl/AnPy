import Functions as F
import time
import matplotlib.pyplot as plt

number_of_calls = 10001
x_values = []
y_values_replace = []
y_values_buffered = []


def test7():
    print(
        f"Measure and compare the time needed to calculate {number_of_calls-1}-th fibonacci-numbers with iterative functions")

    F.instantiate_buffer(number_of_calls)
    total_time = 0

    for i in range(number_of_calls):

        x_values.append(i)

        start_time = time.perf_counter_ns()
        fib_result = F.fib_iterative_replace(i)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        print(f"REPLACE - {i}.te Fibonacci-Number: {fib_result}; Time needed: {duration}")
        y_values_replace.append(duration)

        start_time = time.perf_counter_ns()
        fib_result = F.fib_iterative_buffered(i)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        print(f"BUFFERED - {i}.te Fibonacci-Number: {fib_result}; Time needed: {duration}")
        y_values_buffered.append(duration)
        total_time += duration

    average_time = total_time / number_of_calls
    print(f"Average time needed: {round(average_time)} in nanoseconds")

    plt.xlabel("n-th Fibonacci Number")
    plt.ylabel("Time needed in Nanoseconds")

    plt.plot(x_values, y_values_buffered, label='Buffered-Function', color='red')
    plt.plot(x_values, y_values_replace, label='Replace-Function', color='green')

    plt.legend()
    plt.show()


test7()
