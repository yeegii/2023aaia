class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()#先把數字排好
        ans = [[nums[0]]] #把最前面最小的數字放在兩層方括號裡
        repeat = 0 #目前的數字nums[0]沒有重複
        N = len(nums)
        for i in range(1,N): #比較nums[i] vs.nums[i-1]是否相同
            if nums[i] == nums[i-1]:
                repeat +=1
                if len(ans)<=repeat:#目前層數不夠
                    ans.append( [] )  #增加一層樓
            else: #沒有重複
                repeat = 0
            ans[repeat].append( nums[i] )
        return ans