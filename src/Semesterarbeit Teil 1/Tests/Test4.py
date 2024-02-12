import Functions as F
import matplotlib.pyplot as plt
import time

number_of_calls = 1001
x_values = []
y_values = []
buffer = []


def test4():
    print(
        f"Measure the time needed to calculate the n-th fibonacci-number with buffered recursive function")

    F.instantiate_buffer(number_of_calls)

    for i in range(number_of_calls):
        start_time = time.perf_counter_ns()
        fib_result = F.buffered_fib(i)
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
