numbers = [12, 35, -23, 67]

count = 0
total = 0
for n in numbers:
    total = total + n
    count = count + 1

print(total / count)

#EXPECT 22.75

print(sum(numbers) / len(numbers))