# 답안 예시
# H 입력 받기
h = int(input())

count = 0

# i: 시, j: 분, k: 초
for i in range (h + 1):
	for j in range(60):
		for k in range(60):
			# 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
			if '3' in str(i) + str(j) + str(k):
				count += 1

print(count)