def handle(req):
    # Perform a CPU-intensive operation (in this case, calculating prime numbers)
    primes = []
    for i in range(2, 100000):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    # Return the calculated primes as a string
    return str(primes)
