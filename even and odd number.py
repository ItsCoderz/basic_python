list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_count, even_count = 0, 0
for num in list1:
    if num % 2 == 0:
        odd_count += 1
    else:
        even_count += 1
print("odd numbers in the list: ", even_count)
print("even numbers in the list: ", odd_count)
