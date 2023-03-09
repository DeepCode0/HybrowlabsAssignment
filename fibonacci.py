def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Initialize variables
    prev = 0
    curr = 1

    # Compute nth Fibonacci number
    for i in range(2, n+1):
        next = prev + curr
        prev = curr
        curr = next

    return curr
