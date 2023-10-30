#Given list
digits = [8, 3, 5, 1]
result = 0
multiplier = 1

#Iterate through the list of digits in reverse order
for digit in reversed(digits):
    result += digit * multiplier
    multiplier *= 10

print(result)