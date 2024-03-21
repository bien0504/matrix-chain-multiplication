import random

def init_random_data(n, a, b, filename='input.txt'):
    """Initialize random data and save it to a file."""
    random_numbers = [random.randint(a, b) for _ in range(n)]
    random_numbers_str = ",".join(map(str, random_numbers))
    with open(filename, 'w') as file:
        file.write(random_numbers_str)

def get_data(filename='input.txt'):
    """Read data from the file."""
    try:
        with open(filename, 'r') as file:
            data = file.read().split(',')
        return [int(num) for num in data]
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
# def write_result(x, y):
#     """Write x and y values to output.txt file."""
#     with open('ouput.txt', 'w') as file:
#         file.write(f"x: {x}\n")
#         file.write(f"y: {y}\n")

if __name__ == "__main__":
    init_random_data(10, 1, 100)

    data = get_data()
    if data:
        print("Data from file:", data)
