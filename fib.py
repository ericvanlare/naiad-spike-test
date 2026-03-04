# fib.py — Compute Fibonacci numbers using an iterative approach.
#
# The Fibonacci sequence is defined as:
#   F(0) = 0
#   F(1) = 1
#   F(n) = F(n-1) + F(n-2)  for n >= 2
#
# This implementation uses O(1) space and O(n) time.


def fib(n):
    """Return the nth Fibonacci number.

    Args:
        n (int): The index in the Fibonacci sequence (0-indexed).
                 Must be a non-negative integer.

    Returns:
        int: The nth Fibonacci number.

    Examples:
        >>> fib(0)
        0
        >>> fib(1)
        1
        >>> fib(10)
        55
    """
    # Base case: F(0) = 0
    if n <= 0:
        return 0
    # Base case: F(1) = 1
    elif n == 1:
        return 1

    # Iterative computation:
    # We keep track of two consecutive Fibonacci numbers (a, b)
    # and advance them forward through the sequence.
    a, b = 0, 1  # a = F(0), b = F(1)
    for _ in range(2, n + 1):
        # Shift forward: a becomes the old b, b becomes a + b (the next Fibonacci number)
        a, b = b, a + b

    # b now holds F(n)
    return b


# When run as a script, print the first 10 Fibonacci numbers.
if __name__ == "__main__":
    for i in range(10):
        print(f"fib({i}) = {fib(i)}")
