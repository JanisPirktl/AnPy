import decimal


# Calculates desired decimal places of square root of 5
def set_precision(precision):
    decimal.getcontext().prec = precision
    five = decimal.Decimal(5)
    return five.sqrt()


# Enhanced Function with Binet's formula, able to calculate higher fibonacci-numbers
def fib_binet_precision(n, sqrt_of_5):
    golden_ratio = (1 + sqrt_of_5) / 2
    return round((golden_ratio ** n - (1 - golden_ratio) ** n) / sqrt_of_5)


def fib_iterative_replace(n):
    if n <= 1:
        return n
    fib_numbers = [0, 1]
    for i in range(1, n):
        current = fib_numbers[0]
        fib_numbers[0] = fib_numbers[1]
        fib_numbers[1] = current + fib_numbers[0]
    return fib_numbers[1]


def fib_iterative_append(n):
    if n <= 1:
        return n
    fib_numbers = [0, 1]
    for i in range(1, n):
        fib_numbers.append((fib_numbers[-1] + fib_numbers[-2]))
    return fib_numbers[-1]


number_of_calls = 1005


def code8():
    print(f"Calculate {number_of_calls-1} fibonacci-numbers with enhanced binet's formula and check for correctness")

    sqrt_of_5 = set_precision(212)

    for i in range(number_of_calls):
        fib_result_binet = fib_binet_precision(i, sqrt_of_5)
        fib_result_replace = fib_iterative_replace(i)
        fib_result_append = fib_iterative_append(i)
        print(f"BINET -   {i}.te Fibonacci-Number: {fib_result_binet}")
        print(f"REPLACE - {i}.te Fibonacci-Number: {fib_result_replace}")
        print(f"APPEND -  {i}.te Fibonacci-Number: {fib_result_append}")

        if fib_result_binet != fib_result_replace or fib_result_binet != fib_result_append:
            print(f"RESULTS DO NOT MATCH AT {i}-th NUMBER!")


code8()
