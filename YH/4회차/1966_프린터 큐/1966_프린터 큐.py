import sys

def split_arr(arr, m, count):
    high_idx = arr.index(max(arr))

    if high_idx == m:
        print(count)
    else:
        count += 1
        high = arr[high_idx + 1:]
        low = arr[:high_idx]
        arr2 = high + low

        if m < high_idx:
            m += len(high)
        elif m > high_idx:
            m -= len(low) + 1

        split_arr(arr2, m, count)

k = int(input())

for i in range(k):
    inp = sys.stdin.readline().rstrip()
    n, m  = map(int, inp.split())
    inp2 = sys.stdin.readline().rstrip()
    arr = list(map(int, inp2.split()))

    count = 1
    idx = split_arr(arr, m, count)