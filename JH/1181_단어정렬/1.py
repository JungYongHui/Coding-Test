#%%
import sys

input1= input()
input2 = sys.stdin.readlines()

input2 = set(input2)

key= lambda x: (len(x),x)

print(*sorted(input2,key=key),sep='')