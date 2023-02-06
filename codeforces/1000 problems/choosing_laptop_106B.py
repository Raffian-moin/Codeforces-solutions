n = int(input())

arr = {}

speed = 0
ram = 0
hdd = 0

for i in range(1, n+1):
  s, r, h, c = list(map(int, input().split()))
  speed = max(speed, s)
  ram = max(ram, r)
  hdd = max(hdd, h)
  arr[i] = [s, r, h, c]

cost = 1000
k = 0

for key, value in arr.items():
    if value[0]>=speed or value[1]>=ram or value[2]>=hdd:
      cost = min(cost, value[3])
      if cost == value[3]:
        k = key

print(k)
