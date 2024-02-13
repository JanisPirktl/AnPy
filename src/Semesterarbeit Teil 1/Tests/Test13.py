import Functions as F
import time
import matplotlib.pyplot as plt

number_of_calls = 72
x_values = []
y_values_buffered = []
y_values_binet = []
buffer = []


def test13():
    print(
        f"Measure and compare the time needed to calculate {number_of_calls-1}-th fibonacci-numbers with different functions")

    F.instantiate_buffer(number_of_calls)

    for i in range(number_of_calls):

        x_values.append(i)

        start_time = time.perf_counter_ns()
        fib_result = F.fib_iterative_buffered(i)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        print(f"BUFFERED - {i}.te Fibonacci-Number: {fib_result}; Time needed: {duration}")
        y_values_buffered.append(duration)


        start_time = time.perf_counter_ns()
        fib_result = F.fib_binet(i)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        print(f"BINET - {i}.te Fibonacci-Number: {fib_result}; Time needed: {duration}")
        y_values_binet.append(duration)


    plt.xlabel("n-th Fibonacci Number")
    plt.ylabel("Time needed in Nanoseconds")

    plt.plot(x_values, y_values_buffered, label='Buffered-Function', color='red')
    plt.plot(x_values, y_values_binet, label='Binet-Function', color='blue')

    plt.legend()
    plt.show()


test13()