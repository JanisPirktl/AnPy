import Functions as F
import matplotlib.pyplot as plt
import time

number_of_calls = 31
x_values = []
y_values = []


def test3():
    print(f"Measure the time needed to calculate the n-th fibonacci-number with recursive function")

    for i in range(number_of_calls):
        counter = F.fib_calls(i, [0])[1]
        start_time = time.perf_counter_ns()
        fib_result = F.fib(i)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        print(f"{i}.te Fibonacci-Number: {fib_result}; Number of calls: {counter[0]}; Time needed: {duration}")
        x_values.append(i)
        y_values.append(duration)

    plt.xlabel("n-th Fibonacci Number")
    plt.ylabel("Time needed in Nanoseconds")

    plt.plot(x_values, y_values, color='black')
    plt.show()


test3()