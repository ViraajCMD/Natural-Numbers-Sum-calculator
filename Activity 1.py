print("Welcome to the Natural Number sum calculator!")

n = int(input("\nPlease enter a natural number: "))

sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1

print("\nThe sum of the first", n, "natural numbers is:", sum)

print("\nThank you for using the Natural Number sum calculator!")