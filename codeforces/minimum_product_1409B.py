a, b, x, y, n = list(map(int, input().split()))

dic = {
    a: x,
    b: y
}

minimum = min(a, b)
maximum = max(a, b)
remain = minimum-dic[minimum]
print(remain)
if (remain < n):
    # b = b-remain
    z = minimum-remain
    p = maximum-(n-remain)
    # a = a-(n-remain)
else:
    z = minimum-remain
# print(a, b)
print(z*p)