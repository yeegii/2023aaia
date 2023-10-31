 if n <=0:
            return False
        while n>1:
            if n % 2 !=0: #餘數不是零
               return False

            else:
             n =n//2   #要變小

        return True