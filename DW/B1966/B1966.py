import sys

f_input = int(sys.stdin.readline())

for _ in range(f_input):
    printing = list(map(int, sys.stdin.readline().split()))
    print_list = list(range(printing[0]))
    imp = list(map(int, sys.stdin.readline().split()))
    print_list[printing[1]] = 'target'
    
    order = 0
    while True:
        if imp[0] == max(imp):
            order += 1
            if print_list[0] == 'target':
                print(order)
                break
            else:
                print_list.pop(0)
                imp.pop(0)
        else:
            print_list.append(print_list.pop(0))
            imp.append(imp.pop(0))
