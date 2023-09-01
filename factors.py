import sys

def factorize(num):
    for i in range(2, num):
        if num % i == 0:
            return i, num // i
    return None, None

if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)

input_file = sys.argv[1]

try:
    with open(input_file, 'r') as file:
        for line in file:
            num = int(line.strip())
            p, q = factorize(num)
            if p is not None and q is not None:
                print(f"{num}={p}*{q}")
except FileNotFoundError:
    print(f"File '{input_file}' not found.")
    sys.exit(1)
except ValueError:
    print("Invalid input in the file. Please make sure all lines are valid natural numbers greater than 1.")
    sys.exit(1)
