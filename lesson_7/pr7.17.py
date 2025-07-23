n = int(input())
total = 1

for i in range(1, n+1):
    m = int(input())
    if m != 0:
        total *= m
print(total)
