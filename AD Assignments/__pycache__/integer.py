n = int(input("Please enter a positive integer: "))

print("Numbers from 1 to", n, ":")
for i in range(1, n + 1):
    print(i)

sum_of_numbers = 0
current_number = 1

while current_number <= n:
    sum_of_numbers += current_number
    current_number += 1

print("The sum of all numbers from 1 to", n, "is:", sum_of_numbers)