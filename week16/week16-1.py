class Solution:
    def maxScore(self, s: str) -> int:
        #for left in range(N-1) 0...left左邊 右邊left+1...N-1
        N = len(s)#字串長度
        ans = 0
        for left in range(N-1):
            #接下測測看左邊幾個0 右邊幾個1
            now=0 #測試的值
            for i in range(N): #每個字母都檢查
                if i <=left and s[i]=='0':now+=1 #左邊的0，成功
                if i >left and s[i]=='1':now +=1 #右邊的1，成功
            if now>ans: ans=now #迴圈中間，更新答案
        return ans