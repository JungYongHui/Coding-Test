import sys

T = int(sys.stdin.readline())

for i in range(T):
    func = str(sys.stdin.readline())
    length = int(sys.stdin.readline())
    arr_str = str(sys.stdin.readline().rstrip())

    if len(arr_str) == 2:
        arr = []
    else:
        arr = list(map(int, arr_str[1:-1].split(',')))

    for j in range(len(func)):
        if func[j] == 'R':
            arr.reverse()
        elif func[j] == 'D':
            if len(arr) == 0:
                print('error')
            else:
                del arr[0]

    if len(arr) != 0:
        print(arr)