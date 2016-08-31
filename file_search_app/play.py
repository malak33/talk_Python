
# recursion
# 5! = 120:
# 5 * 4 * 3 * 2 * 1

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print("5!={:,}, 3!={:,}, 11!={:,}".format(
    factorial(5),   # 120
    factorial(3),    # 6
    factorial(11)   # HUGE
))


# Fibonacci numbers:
# 1, 1, 2, 3, 5, 8, 13, 21

def fibonacci_co(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        yield current

    return nums

print(fibonacci_co(100))
print()
for n in fibonacci_co(100):
    print(n, end=', ')
