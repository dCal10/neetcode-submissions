class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]


        maxPrev, maxCurr = nums[0], max(nums[0], nums[1])

        # loop from 2 to n:
        for i in range(2, n):
            maxPrev, maxCurr = maxCurr, max(maxPrev + nums[i], maxCurr)
            

        return maxCurr
