odd = 3
add = False
loop = 100000
total = 1


for i in range(loop):
  if add == False:
    total = total - 1/odd
    odd += 2
    add = True
  else:
    total = total + 1/odd
    odd +=2
    add = False

total = total *4

print(str(total))
