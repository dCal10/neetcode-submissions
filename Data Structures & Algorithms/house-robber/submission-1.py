class Solution:
    def rob(self, nums: List[int]) -> int:
        # set nums second to last
        n = len(nums)
        nums[n - 2] = max(nums[n -1], nums[n - 2])
        #return if n == 2
        if n == 2: return nums[n - 2]
        #go from third to last down to 0
        for i in range(n - 3, -1, -1):            
            nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])
        return nums[0]