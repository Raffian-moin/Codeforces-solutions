n = int(input())
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))

l = set(list1).union(set(list2))
count = 0
flag=0

for i in l:
    if abs(list1.count(i)-list2.count(i))%2==1:
        flag=1
        break
    else:
        count+=abs(list1.count(i)-list2.count(i))

print(-1 if flag==1 or count%4 != 0 else count//4)