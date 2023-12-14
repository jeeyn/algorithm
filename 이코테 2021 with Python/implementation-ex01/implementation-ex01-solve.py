# 내 풀이 답안
n = int(input())
move = input().split()
x, y = 1, 1

for m in move:
	if m == 'L':
		if y != 1:
			y -= 1
	elif m == 'R':
		if y != n:
			y += 1
	elif m == 'U':
		if x != 1:
			x -= 1
	elif m == 'D':
		if x != n:
			x += 1
		
print(x, y)