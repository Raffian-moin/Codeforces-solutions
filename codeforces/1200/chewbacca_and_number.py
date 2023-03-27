n=list(input((" ")))
 
for i in range(1, len(n)):
    if int(n[i])>=5:
        n[i]=str(9-int(n[i]))
 
if int(n[0])>=5 and int(n[0])!=9:
    n[0]=str(9-int(n[0]))
 
print(''.join(n))


# can also be written as 
# v=[min(int(x),9-int(x)) for x in raw_input()]
# if v[0]<1:v[0]=9
# print ''.join(map(str,v))
