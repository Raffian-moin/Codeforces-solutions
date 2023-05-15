
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    a=sorted(list(map(int, input().split())))
    x=a[-5]*a[-4]*a[-3]*a[-2]*a[-1]
    print(max(x, a[-1]*a[0]*a[1]*a[2]*a[3], a[-3]*a[-2]*a[-1]*a[0]*a[1]))