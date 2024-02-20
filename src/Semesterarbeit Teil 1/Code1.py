number_of_calls = 31


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def code1():
    print(f"Calculate {number_of_calls-1} fibonacci-numbers with recursive function")
    for i in range(number_of_calls):
        fib_result = fib(i)
        print(f"{i}.te Fibonacci-Number: {fib_result}")


code1()
