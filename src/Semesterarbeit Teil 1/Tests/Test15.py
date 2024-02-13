import Functions as F
import time
import matplotlib.pyplot as plt

number_of_calls = 1004
buffer = []


def test13():
    print(
        f"Demonstrate the incorrectnes for results with binet's formula")

    F.instantiate_buffer(number_of_calls)
    sqrt_of_5 = F.set_precision(212)

    for i in range(number_of_calls):



        start_time = time.perf_counter_ns()
        fib_result = F.fib_iterative_buffered(i)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        print(f"BUFFERED - {i}.te Fibonacci-Number: {fib_result}; Time needed: {duration}")


        start_time = time.perf_counter_ns()
        fib_result = F.fib_binet_precision(i, sqrt_of_5)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        print(f"BINET - {i}.te Fibonacci-Number: {fib_result}; Time needed: {duration}")



test13()