# Initialize the starting Fibonacci sequence with the first two terms
fibs = [0, 1]

# Print a header for the Fibonacci sequence project
print("Project One (01) - Part A : Fibonacci Sequence")

# Get the user input for the number of terms in the sequence
n = int(input("Sequence ends at:  "))

# Generate the Fibonacci sequence up to the specified number of terms
for i in range(n - 1):
    fibs.append(fibs[-1] + fibs[-2])

# Print the generated Fibonacci sequence with formatting
for i in range(len(fibs)):
    print("{}: {} {}".format(i, fibs[i], format(fibs[i], ',d')))

# Print a blank line for separation
print()

# Print the end message for the project
print("END: Project One (01) - Part A")
print("Shuo You syou45 251274673")
