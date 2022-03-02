a, b = map(int, input().split())

a_yak = []
b_yak = []

mina_b = min(a,b)
maxa_b = max(a,b)

# 최대공약수 구하기
for i in range(mina_b, 1, -1):
    if mina_b % i == 0 and maxa_b % i == 0:
        print(i)
        break

# 최소공배수 구하기
num = 1
while True:
    