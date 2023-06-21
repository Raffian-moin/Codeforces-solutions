n=int(input())
a=sorted(list(map(int, input().split())))
m=sum(a)
if m/n>=4.5:
    print(0)
else:
    for i in range(n):
        m+=5-a[i]
        if m/n>=4.5:
            print(i+1)
            break

print(m)

# can also be written as
# ans=0
# while m/n<4.5:
#     m+=5-a[ans]
#     ans+=1
# print(ans)

