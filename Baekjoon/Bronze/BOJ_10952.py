# https://www.acmicpc.net/problem/10952
# Bronze 5 A+B - 5

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a + b)