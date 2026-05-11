class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for num in range(n+1):
            res = 0
            while num:
                num &= num - 1
                res += 1
            ans.append(res)
        return ans