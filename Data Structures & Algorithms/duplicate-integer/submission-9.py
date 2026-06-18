from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ''' freq = defaultdict(int)
        for num in nums:
            if freq[num] == 1:
                return True
            freq[num] += 1
        return False '''
        nums.sort()
        for index, num in enumerate(nums):
            if index == len(nums) - 1:
                continue
            if num == nums[index + 1]:
                return True
        return False
        