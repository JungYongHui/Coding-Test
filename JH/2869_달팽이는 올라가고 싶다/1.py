a,b,v = map(int,input().split())
x,y=divmod(v-b,a-b)
print(x+bool(y))