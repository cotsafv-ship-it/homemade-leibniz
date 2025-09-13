import math

x = 3.14
accuracy = 15
count = 3
total = x
sign = -1

for i in range(accuracy):
    total += float(sign*(((x)**count)/math.factorial(count)))
    count += 2
    sign = -sign

print(total)
