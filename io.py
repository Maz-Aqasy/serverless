import os

def handle(req):
    # Get the path to the file from the input
    file_path = req

    # Read the contents of the file
    with open(file_path, 'r') as file:
        data = file.read()

    # Modify the data in some way
    new_data = data.upper()

    # Write the modified data back to the file
    with open(file_path, 'w') as file:
        file.write(new_data)

    # Return a message indicating success
    return "File processed successfully"

