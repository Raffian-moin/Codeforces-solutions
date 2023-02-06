MyList = [1, 1, 2, 2, 3, 3]
flag = 1
for i in MyList:
    print(i)
    if MyList.count(i)%2 != 0:
        flag = 0
        break

if flag == 0:
    print(-1)
else:
    for i in range(1, 2):
        last = MyList[0]
        MyList[i-1] = MyList[i]
    
    MyList[len(MyList)-1] = last