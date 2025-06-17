m = int(input())
p = int(input())
d = int(input())

for i in range(d):
    print(i + 1, ".", m)
    pr = m * p / 100
    m = m + pr 
