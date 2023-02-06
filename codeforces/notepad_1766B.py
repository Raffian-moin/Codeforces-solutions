st = 'uohhhhhhh'

operation = 10

count = 0

for i in range(len(st)):
    if st.count(st[i:i+2]) > 1 and len(set(st[i:i+3])) != 1:
        count =1
        break

print('YES' if count==1 else 'NO')