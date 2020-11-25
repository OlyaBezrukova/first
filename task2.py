a, b = int(input()), int(input())
for i in range(a, b+1):
    th = i // 1000
    h = (i // 100) % 10
    d = (i // 10) % 10
    e = i % 10
    if th == e and h == d:
        print(i, end=' ')
