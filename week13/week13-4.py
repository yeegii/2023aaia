class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0

        while n>0: #要把n剝光光
            ans += n%2 #撥下來的皮
            n = n //2 #n播完就變小了

        return ans #迴圈後面ans拿來用