def sekanten_trapez_regel(f, a, b, n):
    delta_x = (b - a) / n
    integral = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        x_i = a + i * delta_x
        integral += f(x_i)

    integral *= delta_x
    return integral


def tangenten_trapez_regel(f, a, b, n):
    delta_x = (b - a) / n
    def derivat(f, x, h=1e-5):
        return (f(x + h) - f(x - h)) / (2 * h)

    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x_i = a + i * delta_x
        integral += f(x_i)

    for i in range(n):
        x_i = a + i * delta_x
        x_ip1 = x_i + delta_x
        integral += (delta_x ** 2 / 12) * (derivat(f, x_i) - derivat(f, x_ip1))

    integral *= delta_x
    return integral


def simpson_regel(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Die Anzahl der Doppelstreifen n muss gerade sein.")

    delta_x = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n):
        x_i = a + i * delta_x
        if i % 2 == 0:
            integral += 2 * f(x_i)
        else:
            integral += 4 * f(x_i)

    integral *= delta_x / 3
    return integral
