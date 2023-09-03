positive_count = 0
negative_count = 0

while True:
    try:
        value = int(input("Enter an integer value (0 to terminate): "))
        if value == 0:
            break
        if value > 0:
            positive_count += 1
        elif value < 0:
            negative_count += 1
    except ValueError:
        print("Invalid input. Please enter an integer value.")

print("Positives: " + "*" * positive_count)
print("Negatives: " + "*" * negative_count)
