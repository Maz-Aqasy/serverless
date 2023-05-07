def handle(req):
    # Perform a CPU-intensive operation
    result = 0
    for i in range(100000000):
        result += i

    # Return the result
    return f"Result: {result}"
