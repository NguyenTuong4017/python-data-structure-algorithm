def fib(n):
    if n < 2:
        return 1
    prev = prev_prev = 1
    for _ in range(n - 1):
        result = prev + prev_prev
        prev, prev_prev = result, prev
    return result


print(fib(10))
