from itertools import accumulate
import bisect

for _ in range(int(input())): 
    n, q = list(map(int, input().split()))
    a = sorted(list(map(int, input().split())), reverse=True)
    acc = list(accumulate(a))

    for i in range(q):
        k=int(input())
        print (-1 if k>acc[-1] else bisect.bisect_left(acc, k)+1)