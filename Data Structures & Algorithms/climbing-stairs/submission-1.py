class Solution:
    def climbStairs(self, n: int) -> int:
        # base cases of prev, curr for n = 1, 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev, curr = 1, 2
        # loop trhough (3 to n+1)
        for i in range(3, n + 1):
        # update prev, curr to curr, prev + cur
            prev, curr = curr, prev + curr
        
        # return curr
        return curr