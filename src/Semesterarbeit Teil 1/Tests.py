import time
import Functions as F

# Number of Fibonacci numbers to calculate
number_of_calls = 1001

# Number of Fibonacci numbers to calculate with recursive
number_of_calls_for_recursive = 31

total_time_buffered = 0
total_time_dynamic = 0
total_time_iterative_append = 0
total_time_iterative_replace = 0

def test1111():
    print(f"Calculate the {number_of_calls_for_recursive} first fibonacci-numbers with recursive function")
    for i in range(number_of_calls_for_recursive):
        counter = F.fib_calls(i, [0])[1][0]
        start_time = time.perf_counter_ns()
        fib_result = F.fib(i)
        end_time = time.perf_counter_ns()
        duration_recursive = end_time - start_time
        print(
            f"{i}.te Fibonacci-Number:          {fib_result};      Needed time: {duration_recursive} nanoseconds;         Number of calls: {counter}")


def test2111():
    print(f"Calculate the {number_of_calls} first fibonacci-numbers with buffered recursive function")
    F.instantiate_buffer(number_of_calls)
    global total_time_buffered

    for i in range(number_of_calls):
        start_time = time.perf_counter_ns()
        fib_result = F.buffered_fib(i)
        end_time = time.perf_counter_ns()
        duration_buffered = end_time - start_time
        total_time_buffered += duration_buffered
        print(
            f"{i}.te Fibonacci-Number:          {fib_result};      Needed time: {duration_buffered} nanoseconds;")



def test3111():
    print("Calculate average time needed with binet's formula if the function is alone in the loop")
    print(
        "Calculate the 30 first fibonacci-numbers with recursive function in advance to guarantee that the variables needed for binet's formula are not in the data-registers or the caches of the cpu")

    for i in range(number_of_calls_for_recursive):
        fib_result = F.fib(i)

    total_binet_time = 0
    for i in range(number_of_calls_for_recursive):
        start_time = time.perf_counter_ns()
        fib_result = F.fib_binet(i)
        end_time = time.perf_counter_ns()
        duration_binet = end_time - start_time
        total_binet_time += duration_binet
        print(
            f"{i}.te Fibonacci-Number:         {fib_result};        Needed time: {duration_binet} nanoseconds;")
    average_binet_time = total_binet_time / number_of_calls_for_recursive
    print(f"binet needed average time of {round(average_binet_time)} nanoseconds (alone in the loop), no variables needed were in the registers or the caches in advance")


def test4111():
    print("Calculate average time needed with binet's formula if the function is alone in the loop")
    print(
        "Calculate the 30 first fibonacci-numbers with the function that uses binet's formula in advance to check for a difference in the average time need if that the variables needed for binet's formula are already in the data-registers or the caches of the cpu")

    for i in range(number_of_calls_for_recursive):
        fib_result = F.fib_binet(i)

    total_binet_time = 0
    for i in range(number_of_calls_for_recursive):
        start_time = time.perf_counter_ns()
        fib_result = F.fib_binet(i)
        end_time = time.perf_counter_ns()
        duration_binet = end_time - start_time
        total_binet_time += duration_binet
        print(
            f"{i}.te Fibonacci-Number:         {fib_result};        Needed time: {duration_binet} nanoseconds;")
    average_binet_time = total_binet_time / number_of_calls_for_recursive
    print(f"binet needed average time of {round(average_binet_time)} nanoseconds (alone in the loop), the needed variables were in the registers or the caches in advance")


def test5111():
    print("Calculate average time needed with binet's formula if the function is NOT alone in the loop")
    print(
        "Calculate the 30 first fibonacci-numbers with recursive function in advance to guarantee that the variables needed for binet's formula are not in the data-registers or the caches of the cpu")

    for i in range(number_of_calls_for_recursive):
        fib_result = F.fib(i)

    total_binet_time = 0
    for i in range(number_of_calls_for_recursive):
        fib_result = F.fib(number_of_calls_for_recursive)
        start_time = time.perf_counter_ns()
        fib_result = F.fib_binet(i)
        end_time = time.perf_counter_ns()
        duration_binet = end_time - start_time
        total_binet_time += duration_binet
        print(
            f"{i}.te Fibonacci-Number:         {fib_result};      Needed time: {duration_binet} nanoseconds;")
    average_binet_time = total_binet_time / number_of_calls_for_recursive
    print(f"binet needed average time of {round(average_binet_time)} nanoseconds (not alone in the loop), the needed variables were not in the registers or caches in advance")

def test6111():
    start_time = time.perf_counter_ns()
    sqrt_of_5 = F.set_precision(212)
    ent_time = time.perf_counter_ns()
    duration_sqrt_of_5 = ent_time - start_time
    print(f"Time needed to calculate square root of 5 with given precision: {duration_sqrt_of_5}")
    print()
    for i in range(number_of_calls):
        start_time = time.perf_counter_ns()
        fib_result = F.fib_binet_precision(i, sqrt_of_5)
        end_time = time.perf_counter_ns()
        duration_binet_precision = end_time - start_time
        print(f"Binet_precision:      {i}.te Fibonacci-Number:                   {fib_result};       Needed time: {duration_binet_precision} nanoseconds;")
        start_time = time.perf_counter_ns()
        fib_result = F.fib_dynamic(i)
        end_time = time.perf_counter_ns()
        duration_dynamic = end_time - start_time
        print(
            f"Dynamic               {i}.te Fibonacci-Number:                   {fib_result};        Needed time: {duration_dynamic} Nanoseconds;")

def test7111():
    global total_time_dynamic
    for i in range(number_of_calls):
        start_time = time.perf_counter_ns()
        fib_result = F.fib_dynamic(i)
        end_time = time.perf_counter_ns()
        duration_dynamic = end_time - start_time
        total_time_dynamic += duration_dynamic
        print(
            f"{i}.te Fibonacci-Number:                   {fib_result};   Needed time: {duration_dynamic} Nanoseconds;")



def test8111():
    global total_time_iterative_append
    for i in range(number_of_calls):
        start_time = time.perf_counter_ns()
        fib_result = F.fib_iterative_append(i)
        end_time = time.perf_counter_ns()
        duration_iterative_append = end_time - start_time
        total_time_iterative_append += duration_iterative_append
        print(
            f"{i}.te Fibonacci-Number:                   {fib_result};   Needed time: {duration_iterative_append} Nanoseconds;")


def test9111():
    global total_time_iterative_replace
    for i in range(number_of_calls):
        start_time = time.perf_counter_ns()
        fib_result = F.fib_iterative_replace(i)
        end_time = time.perf_counter_ns()
        duration_iterative_replace = end_time - start_time
        total_time_iterative_replace += duration_iterative_replace
        print(
            f"{i}.te Fibonacci-Number:             {fib_result};   Needed time: {duration_iterative_replace} Nanoseconds;")


