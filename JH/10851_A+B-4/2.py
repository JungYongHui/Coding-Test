from sys import stdin

input = lambda: stdin.readlines()

for l in input():
    print(int.__add__(*map(int,l.split())))