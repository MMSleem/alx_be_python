number = int(input("Enter a number to see its multiplication table: "))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(1,11):
    result = number * i
    print(f"{number}* {i} = {result}")