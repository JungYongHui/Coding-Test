import sys

input = sys.stdin.readline
n, k = map(int, input().split()) # 값 입력

def josephus(n: int, k: int) -> int:
    people = [i for i in range(1, n+1)]
    step = k-1 # pop을 고려해서 -1
    i = step
    for _ in range(n):
        try:
            yield people.pop(i) # pop은 index 기준.
        except IndexError:
            i %= len(people) # 나머지 입력
            yield people.pop(i)
        finally:
            i += step

# yield가 값을 반환한다고 생각하면 append가 필요없네!
# 그리고 yield는 계속 나오니, 함수만 실행시키면 n만큼 계속 돌것네!
# *함수 에서 *를 안붙이면 return이 여러개가 되어야할 때 출력이 안되는 듯?

print('<', end = '')
print(*josephus(n, k), sep = ', ', end = '>')