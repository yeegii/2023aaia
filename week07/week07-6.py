s = "abcdabcd"
d = {} #dict字典
for c in s:
  for c in d:
    d[c] = d[c] + 1
  else:
    d[c] = 1
    print('現在讀到的字母', c , "字母變成", d)