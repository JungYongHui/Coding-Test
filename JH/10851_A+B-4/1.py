from sys import stdin

input = lambda: stdin.readlines()
while True:
    try:    
        inp = stdin.readline().split()
        a, b = map(int, inp)
        print(a+b)
    except:
        break