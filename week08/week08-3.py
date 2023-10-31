#剝皮法
a = 1234
ans = 0 #把答案慢慢塞進去
while a>0:
  ans = ans * 10 + a%10
  print('現在的a是', a, '剝出來的皮a%10是',a%10, '現在的 ans 就變成' , ans)
  a= a // 10