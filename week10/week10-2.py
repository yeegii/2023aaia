a = input('請在這裡打一些數字')
a = a.split()
N = len(a)
for i in range(N):
  a[i] = int(a[i])

for i in range(N-1, -1, -1):
  print(a[i])