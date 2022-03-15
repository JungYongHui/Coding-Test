"""def dfs(start, visited):
    visited[start] = True
    print(start, end=' ')

    for w in s:
        print(visited)
        if visited[w] == False:
            dfs(w, visited)


while True:
    inp = list(map(int, input().split()))
    k, s = inp[0], inp[1:]

    if k == 0:
        break

    visited = {i:False for i in s}
    print(k)
    print(s)
    dfs(s[0], visited)

"""
def dfs(count):
    if count == 6:
        for i in s:
            if visited[i] == True:
                print(i, end=' ')
        print()


    for i in s:
        if visited[i] == False:
            visited[i] = True
            count += 1
            dfs(count)
            visited[i] = False
            count -= 1

while True:
    inp = list(map(int, input().split()))
    k, s = inp[0], inp[1:]

    if k == 0:
        break

    visited = {i: False for i in s}
    dfs(0)



