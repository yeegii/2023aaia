if n<=0: #負的一定是錯的
            return False

        while n>1:
            if n % 2 !=0: #有餘數，失敗
                return False #失敗

            n=n//2 #16//2得到8，數字變小

        return True
        