n, k = input().split()

n = int(n)
k = int(k)

count = 0

while True:
    print(n)

    if n == 1:
        break

    if int(n % k) == 0:
        n = n // k
    else:
        n = n - 1

    count = count + 1