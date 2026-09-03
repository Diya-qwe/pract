import sys

# If a number is provided as a command‑line argument, use it; otherwise default to 5
n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"Factorial of {n} is {fact}")