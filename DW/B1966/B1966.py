# import sys


# f_input = int(sys.stdin.readline())

# for _ in range(f_input):
#     n, t = list(map(int ,sys.stdin.readline().split()))
#     printing = ['x' for _ in range(n)]
#     printing[t] = 'target'
#     important = list(map(int, sys.stdin.readline().split()))

#     order = 0

#     for imp in important:
#         if imp == max(important):
#             order +=1

#             if printing[0] == 'target':
#                 print('답:',order)
#                 break

#             else:
#                 printing.pop(0)
#                 important.pop(0)
#         else:
#             important.append(important.pop(0))
#             printing.append(printing.pop(0))

test_cases = int(input())

for _ in range(test_cases):
    n,m = list(map(int, input().split(" ")))
    imp = list(map(int, input().split(" ")))
    idx = list(range(len(imp)))
    idx[m] = 'target'

    # 순서
    order = 0
       
    for x in imp:
        if x==max(imp):
            order += 1
                           
            if idx[0]=='target':
                print(order)
                break
            else:
                imp.pop(0)
                idx.pop(0)

        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))
