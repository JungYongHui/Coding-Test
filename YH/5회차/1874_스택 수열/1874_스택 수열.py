n = int(input())
num = 0
stack = []
func_list = []
temp = True

for _ in range(0, n):
    x = int(input())
    print(x)

    while num < x:
      num += 1
      stack.append(num)
      func_list.append("+")

    if stack[-1] == x:
        stack.pop()
        func_list.append("-")
    else:
        temp = False
        break

if temp == False:
    print("NO")
else:
    for i in func_list:
        print(i)
