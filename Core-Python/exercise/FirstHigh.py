numbers = [100, 10, 11, 5, 13, 17, 88]

highest = numbers[0]   # pehle element ko hi highest maan lo

for num in numbers:
    if num > highest:
        highest = num

print("Highest number is:", highest)