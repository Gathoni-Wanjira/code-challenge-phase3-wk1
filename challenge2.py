 # Taking user input for the three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

def exactly_two_positive(a, b, c):
    positive_count = 0

    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    return positive_count == 2
         
result = exactly_two_positive(a, b, c)
print(f"Exactly two out of the three numbers are positive: {result}")



    
    