def handle(req):
    # Allocate a large amount of memory
    data = bytearray(1000000000)  # 1 billion bytes

    # Manipulate the data in some way
    for i in range(len(data)):
        data[i] = i % 256

    # Return a message indicating success
    return "Memory allocated and manipulated successfully"
