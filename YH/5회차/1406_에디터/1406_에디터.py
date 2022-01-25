import sys

origin = input()
n = int(input())

def cur_left(cur_idx, ans):
    if cur_idx == 0:
        return cur_idx, ans
    else:
        cur_idx -= 1
        return cur_idx, ans

def cur_right(cur_idx, ans):
    if cur_idx >= len(ans):
        return cur_idx, ans
    else:
        cur_idx += 1
        return cur_idx, ans

def del_left(cur_idx, ans):
    if cur_idx == 0:
        return cur_idx, ans
    else:
        cur_idx -= 1
        ans = ans[:cur_idx] + ans[cur_idx+1:]
        return cur_idx, ans

def add_left(cur_idx, ans, text):
    ans = ans[:cur_idx] + text + ans[cur_idx:]
    cur_idx += 1
    return cur_idx, ans

func_dict = {'L':cur_left,
             'D':cur_right,
             'B':del_left,
             'P':add_left}

ans = origin
cur_idx = len(ans)

for _ in range(n):
    func, *text = sys.stdin.readline().rstrip().split()
    cur_idx, ans = func_dict[func](cur_idx, ans, *text)

print(ans)
