

numbers = [12, 5, 8, 23, 7, 15, 3, 19]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even count: {even_count}")
print(f"odd count: {odd_count}")
