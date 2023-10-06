# Print a header for the Prime Numbers project
print("Part One - Project B: Prime Choice")

# Get user input for the range of prime numbers
start = int(input("Prime Numbers starting with: "))
end = int(input("and ending with: "))

# Ensure that start is less than or equal to end
if start > end:
    print()
    print("Incorrect Input: {} is greater than {}".format(start, end))
    print("The numbers have been automatically switched.")
    start, end = end, start

print()  # Print a blank line for separation

# Function to check if a number is prime
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Print the prime numbers within the specified range
print(f"Prime numbers in the range from: {start} and {end} are:")
for i in range(start, end):
    if isPrime(i):
        print(f"{i} is a prime")

print()  # Print a blank line for separation

# Print the end message for the project
print("END: Project One (01) - Part B")
print("Shuo You syou45 251274673")
