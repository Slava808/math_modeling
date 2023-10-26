n = int(input())
first = 1
second = 1
print(first, end=" ")
for _ in range(n-1):
    temp = first + second
    first = second
    second = temp
    print(second, end=" ")