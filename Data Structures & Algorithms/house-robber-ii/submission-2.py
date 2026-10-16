class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3: return max(nums)
        #take max of nums[0] to nums[n-2] and nums[1] to nums[n-1] 
        def robsLine(first: int, last: int) -> int:
            prev, curr = nums[first], max(nums[first], nums[first + 1])
            for i in range(first + 2, last + 1):
                prev, curr = curr, max(curr, nums[i] + prev)
            return curr
        maxC1 = robsLine(0, n-2)
        maxC2 = robsLine(1, n-1)
        return max(maxC1, maxC2)
        