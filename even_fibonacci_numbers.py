first = 1
second = 1
sum = 0
while first <= 4000000:
    if first % 2 == 0:
        sum += first
    first, second = second, first + second
print(sum)