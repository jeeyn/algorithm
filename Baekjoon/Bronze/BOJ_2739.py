# https://www.acmicpc.net/problem/2739
# Bronze 5 구구단

n = int(input())

for i in range(1, 10):
    print("%d * %d = %d" %(n, i, n * i))