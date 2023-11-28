a = 1080000000 #把數字變很大 老大
b = 2000000000 #也把數字變很大 老二
c = a%b 
print(a ,b, c)
while c!=0: #輾轉相除法
  a = b #老二變老大
  b = c #老三變老二
  c = a%b #新的老三算出來
  print(a ,b ,c)
print(b)
