def unit(x):
    x = x % 1000
    x = x % 100
    x = x % 10
    return x


def ten(x):
    x = x % 1000
    x = x % 100
    x = x // 10
    return x


def swap_unit_ten(x):
    a = x // 100 * 100
    b = unit(x) * 10
    c = ten(x)
    return a + b + c

