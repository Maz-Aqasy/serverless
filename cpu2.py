def handle(req):
    # Perform a computationally-intensive operation
    result = 0
    for i in range(1000000):
        result += i**2

    # Return the result
    return str(result)
