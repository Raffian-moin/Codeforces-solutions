for _ in range(int(input())):
  n=int(input())
  s = [int(x) for x in input()]
  a=list(map(int, input().split()))
  no_lid_value=0
  c=0
  for i in range(n):
      if s[i]==0:
        no_lid_value=a[i]
      if s[i]==1:
        c+=max(a[i], no_lid_value)
        if a[i]<=no_lid_value:
          # no need for line 14 as we didn't used it
          s[i]=0
          no_lid_value=a[i]

  print(c)
