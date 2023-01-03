
max = 0
while True:
    number = int(input("Enter New Number or 0 to exit"))
    if number > max:
        max = number
    if number == 0:
        break
print(max)