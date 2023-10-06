# Print a header for Project Part C
print("Project One (01) - Part C: The Moore the Merrier")

# Define a dictionary to convert unit prefixes to their corresponding multipliers
unitDef = {
    "": 1,
    "kilo" : 1000,
    "mega" : 1000000,
    "giga" : 1000000000,
    "tera" : 1000000000000,
    "peta" : 1000000000000000,
    "exa"  : 1000000000000000000,
    "zetta": 1000000000000000000000,
    "yotta": 1000000000000000000000000
}

# Get user input for the starting number of transistors, starting year, and total number of years
transistors = int(input("Starting Number of transistors: "))
startYear = int(input("Starting Year: "))
yearNum = int(input("Total Number of Years: "))

# Function to find the appropriate unit for flops
def findUnit(flopNum):
    resultUnit = ""
    for unit in unitDef:
        if flopNum > unitDef[unit]:
            resultUnit = unit
    return resultUnit

# Print a blank line for separation
print()

# Print the header for the data table
print("YEAR : TRANSISTORS : FLOPS:")

# Calculate and print the number of transistors and flops for each year
endYear = startYear + 30
for year in range(startYear, endYear + 1, 2):
    flops = transistors * 50
    unit = findUnit(flops)
    divisor = unitDef[unit]
    print("{} {} {} {}FLOPS {}".format(year, format(transistors, ',d'), format(flops/divisor, ".2f"), unit, format(flops, ',d')))
    transistors = transistors * 2

# Print a blank line for separation
print()

# Print the end message for the project
print("END: Project One (01) - Part C")
print("Shuo You syou45 251274673")
