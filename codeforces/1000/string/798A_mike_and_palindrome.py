s = input()
n = len(s)
count = 0
for i in range(n//2):
    if s[i] != s[n-1-i]:
        count+=1
        
print('YES' if count==1 or (n%2==1 and count==0) else 'NO')