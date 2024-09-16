n = int(input())

for i in range(1, n+1):
    if (i % 2) == 1 and 1 <= i < 1000:
        print(" " * ((n - i) // 2) + "*" * i + " " * ((n - i) // 2))
