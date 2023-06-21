for _ in range(int(input())):
    n = int(input())
    s = input()
    left = 0
    right = 0
    count = 0

    for i in range(n):
        
        if s[i] == '(':
            left+=1
        else:
            right+=1
        if  right > left:
            count+=1
            left = 0
            right = 0

    print(count)

# another answer
#  while '()' in s:
#   s = s.replace('()','')
#  print(len(s)//2)